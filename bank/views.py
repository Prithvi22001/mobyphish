from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import BankUser,Transaction
from django.urls import reverse
import time
from django.conf import settings
import logging
from django.http import HttpResponseRedirect


logger = logging.getLogger('bank')

def bank_login(request):
    bank_logo=settings.MEDIA_URL+'bank-logo.png'
    user_icon=settings.MEDIA_URL+'user-icon.png'

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        password = request.POST.get('password')
        reported = request.POST.get('reported')
        
        if reported:
            request.session['reported']=True
            url=f"https://mobyphish.com/complete_item/"+str(request.session.get('item_id'))+"/"    
            logger.info(f"USER: {user_id} reported {request.build_absolute_uri()}")
            if settings.DEBUG:
                return redirect('complete_item',item_id=request.session.get('item_id'))
            else:
                return redirect(url)



        else:
            request.session['reported']=False


        try:
            user = BankUser.objects.get(user_id=user_id)
            if user.check_password(password):
                request.session['user_id'] = user.user_id
                if request.session.get('task_type')=='airline':
                    to=request.session.get('airline')
                else:
                    to=request.session.get('hotel')

                price=request.session.get('price')
                if price is None or to is None:
                    logger.error(f"USER: {user_id} , session variable not set {request.session.items()}")
                    request.session.flush()
                    message = 'Something went wrong please try again.'
                    request.session.flush()

                    url = 'https://mobyphish.com/login'+ f'?message={message}'
                    response = redirect(url)
                    for cookie in request.COOKIES:
                        response.delete_cookie(cookie)
                    return response
                logger.info(f"USER: {user_id} moving to withdraw page ,to={to} & price={price}")
                url = f"{reverse('withdraw')}?to={to}&price={price}"
                return redirect(url)
            else:
                return render(request, 'log-in.html', {'error': 'Invalid user ID or password.','bank_logo':bank_logo,'user_icon':user_icon})
        except BankUser.DoesNotExist:
            return render(request, 'log-in.html', {'error': 'Invalid user ID or password.','bank_logo':bank_logo,'user_icon':user_icon})
    
    return render(request, 'log-in.html',{'bank_logo':bank_logo,'user_icon':user_icon})

def withdraw(request):
    bank_logo=settings.MEDIA_URL+'bank-logo.png'
    user_icon=settings.MEDIA_URL+'user-icon.png'
    user_id = request.session['user_id']

    if request.method == 'POST':
        to = request.POST.get('to')
        amount = request.POST.get('amount')
        user_id = request.session['user_id']
        reported = request.POST.get('reported')
        if reported:
            request.session['reported']=True
            url=f"https://mobyphish.com/complete_item/"+str(request.session.get('item_id'))+"/"           
            if settings.DEBUG:
                return redirect('complete_item',item_id=request.session.get('item_id'))
            else:
                return redirect(url)

        else:
            request.session['reported']=False

       
        try:
            user = BankUser.objects.get(user_id=user_id)
            transaction = Transaction(user=user, to=to, amount=amount, time_paid=int(time.time()))
            transaction.save()
            logger.info(f"USER: {user_id},  PAID  : {request.session.get('item_id')}")
            url=f"https://mobyphish.com/complete_item/"+str(request.session.get('item_id'))+"/"           
            if settings.DEBUG:
                return redirect('complete_item',item_id=request.session.get('item_id'))
            else:
                return redirect(url)

        except BankUser.DoesNotExist:
            return redirect('bank_login')
    context = {
        'to': request.GET.get('to'),
        'price': request.GET.get('price'),
        'bank_logo':bank_logo,
        'user_icon': user_icon,
        'user_id':user_id,
    }
    return render(request, 'bank-checkout.html',context)

