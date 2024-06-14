from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BankUser,Transaction
from django.urls import reverse
import time

def bank_login(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        reported = request.POST.get('reported')
        
        print(f"BANK SITE REPORTED : {reported}",flush=True)
        if reported:
            request.session['reported']=True
            return redirect('complete_item',item_id=request.session.get('item_id'))
        else:
            request.session['reported']=False


        try:
            user = BankUser.objects.get(user_id=user_id)
            if user.check_password(password):
                # Simulate login (use sessions or another method as per your requirement)
                request.session['user_id'] = user.user_id
                if request.session.get('task_type')=='airline':
                    to=request.session.get('airline')
                else:
                    to="hotel" #request.session.get('airline')

                price=request.session.get('price')
                print(request.session,flush=True)
                url = f"{reverse('withdraw')}?to={to}&price={price}"

                return redirect(url)
            else:
                return render(request, 'bank_login.html', {'error': 'Invalid user ID or password.'})
        except BankUser.DoesNotExist:
            return render(request, 'bank_login.html', {'error': 'Invalid user ID or password.'})
    
    return render(request, 'bank_login.html')

def withdraw(request):
    if request.method == 'POST':
        to = request.POST.get('to')
        amount = request.POST.get('amount')
        user_id = request.session['user_id']
        reported = request.POST.get('reported')
        if reported:
            request.session['reported']=True
            return redirect('complete_item',item_id=request.session.get('item_id'))
        else:
            request.session['reported']=False

       
        try:
            user = BankUser.objects.get(user_id=user_id)
            transaction = Transaction(user=user, to=to, amount=amount, time_paid=int(time.time()))
            transaction.save()
            print(f"ITMR PAID  : {request.session.get('item_id')}")
            return redirect('complete_item',item_id=request.session.get('item_id'))
            return render(request, 'withdraw.html', {'message': 'Withdrawal successful!'})
        except BankUser.DoesNotExist:
            return redirect('bank_login')
    context = {
        'to': request.GET.get('to'),
        'price': request.GET.get('price')
    }
    return render(request, 'withdraw.html',context)

