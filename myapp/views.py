from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Item
from bank.models import BankUser
from .forms import UserIdForm
import time
import urllib.parse
from . import task_generate
from django.conf import settings
import json
import ast
import pickle
import datetime
import random
from datetime import datetime

def home(request):
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            if User.objects.filter(user_id=user_id).exists():
                response = redirect('tasks')
                response.set_cookie('user_id', user_id)
                return response
            else:
                form.add_error('user_id', 'Invalid user ID')
    else:
        form = UserIdForm()
    return render(request, 'home.html', {'form': form})

def logout_view(request):
    response = redirect('home')  # Redirect to home page or any other page
    for cookie in request.COOKIES:
        response.delete_cookie(cookie)
    return response


def items_view(request):
    if 'user_id' not in request.COOKIES:
        return redirect('home')

    user_id = request.COOKIES['user_id']
    user = get_object_or_404(User, user_id=user_id)

    # Check for bank password
    try:
        bank_user = BankUser.objects.get(user_id=user)
        bank_password = bank_user.password
    except BankUser.DoesNotExist:
        bank_password="Could not find bank details!!"
        # return render(request, 'error.html', {'message': 'Bank details not found for user.'})


    default_tasks_count = Item.objects.filter(user=user, status='default').count()
    complete_tasks_count = Item.objects.filter(user=user, status='completed').count()
    active_tasks_count = Item.objects.filter(user=user, status='active').count()
    incorrect_tasks_count = Item.objects.filter(user=user, status='incorrect').count()
    
    total_correct_tasks=complete_tasks_count+active_tasks_count+incorrect_tasks_count
    # Generate tasks only if the number of default tasks is less than 4
    if default_tasks_count+complete_tasks_count+active_tasks_count< 5:

        for i in range(settings.NO_OF_TASKS):
            default_tasks_count = Item.objects.filter(user=user, status='default').count()
            if default_tasks_count+complete_tasks_count +active_tasks_count< 5:
                ans=task_generate.generate_task()
                task=Item(user=user,task=ans['task'],results=pickle.dumps(ans['results']),all_info=pickle.dumps(ans),status='default')
                task.save()
            
    items = Item.objects.filter(user=user)
    active_item = items.filter(status='active').first()

    return render(request, 'items.html', {'items': items, 'active': active_item.id if active_item else None,'bank_password':bank_password,'user_id':user_id})

def proceed_item(request, item_id):
    if 'user_id' not in request.COOKIES:
        return redirect('home')

    user_id = request.COOKIES['user_id']
    user = get_object_or_404(User, user_id=user_id)
    items = Item.objects.filter(user=user)
    item = get_object_or_404(Item, id=item_id)

    active_item = Item.objects.filter(user=user, status='active').first()

    if active_item:
        if active_item.id==item.id:
            print(f"ITEM ID: {item_id} acitve clicked",flush=True)
            return redirect('results',item_id=item_id)
        else:
            print(f"ITEM ID: {item_id} not active clicjed",flush=True)
            messages.error(request, "Cannot start this task until the active task is completed.")
            return redirect('tasks')  # Redirect back to items page

    else:
        if item.status=='active':
            print(f"ITEM ID: {item_id} idk why",flush=True)

            return redirect('results',item_id=item_id)

        else:
            print(f"ITEM ID: {item_id} new active",flush=True)

            item.time_start = int(time.time())
            item.status = 'active'
            item.all_info=item.all_info
            # print(item.all_info,flush=True)
            # print(type(item.all_info),flush=True)
            item.save()
            print(f"Task : {item.id} started at {item.time_start}",flush=True)
            return redirect('results', item_id=item.id)

        # # Redirect to external URL with user_id and task as query parameters
        # base_url = "http://127.0.0.1:8001/results/"
        # params = urllib.parse.urlencode({'user_id': user_id, 'task': item.task,'location':item.location,'travel_industry':item.travel_industry,'item_id':item.id})
        # url = f"{base_url}?{params}"
        # print("REDIRECting",flush=True)        
        # return redirect(url)

        # return render(request, 'redirect_external.html', {'url': url})

        # return redirect('127.0.0.1:8000')

    # return render(request, 'items.html', {'items': items, 'active': active_item.id if active_item else None})



def results(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    all_info=pickle.loads(item.all_info)
    # print("all_info:", repr(all_info), flush=True)
    # print("type of all_info:", type(all_info), flush=True)

    search_results=all_info['results']
    random.shuffle(search_results)
    task=all_info['task']
    task_type = all_info['type']  # Get the type of task
    print(f"search_Results : {search_results}",flush=True)
    


    return render(request, 'results.html', {'task': task, 'task_id': item_id,'search_results':search_results, 'task_type': task_type})

def travel_page(request, item_id):
    if request.method == 'POST':
        task_type = request.POST.get('task_type')
        print(f"in travel view {task_type}", flush=True)

        if task_type == 'hotel':
            from_city = request.POST.get('from_city')
            from_date = request.POST.get('from_date').split(',')[0]
            to_date = request.POST.get('to_date').split(',')[0]
            price = request.POST.get('price')
            ratings=request.POST.get('rating')
            no_of_rooms = request.POST.get('no_of_rooms')
            correct_result = request.POST.get('correct_result') 
            message = request.POST.get('message')
            task_type = request.POST.get('task_type')

            context = {
                'from_city': from_city,
                'from_date': from_date, #datetime.strptime(, "%B %d, %Y, %I:%M %p"),
                'to_date': to_date,#datetime.strptime(to_date, "%B %d, %Y, %I:%M %p"),
                'price': price,
                'no_of_rooms': no_of_rooms,
                'ratings':ratings,
                'correct_result':correct_result,
                'task_type':task_type,
                'message': message,
                'blurb': "Experience the best stay at our luxurious hotel.",
                'blurb1': "Comfortable and well-furnished rooms available.",
                'image': 'path_to_image.jpg',  # Add path to hotel logo image
                'item_id':item_id,
            }
            return render(request, 'hotel_result.html', context)

        elif task_type == 'airline':
            from_city = request.POST.get('from_city')
            to_city = request.POST.get('to_city')
            from_date = request.POST.get('from_date').split(',')[0]
            to_date = request.POST.get('to_date').split(',')[0]
            airline = request.POST.get('airline')
            price = request.POST.get('price')
            message = request.POST.get('message')
            layovers = request.POST.get('layovers')
            correct_result = request.POST.get('correct_result') 
            task_type = request.POST.get('task_type')

            print(from_date,task_type,correct_result,flush=True)
            print(type(from_date),to_date,correct_result,flush=True)

            context = {
                'from_city': from_city,
                'to_city': to_city,
                'from_date':from_date,# datetime.strptime(from_date, "%B %d, %Y, %I:%M %p"),
                'to_date': to_date,#datetime.strptime(to_date, "%B %d, %Y, %I:%M %p"),
                'airline': airline,
                'price': price,
                'layovers': layovers,
                'message': message,
                'correct_result':correct_result,
                'task_type':task_type,
                'item_id':item_id,
                'airline_logo': 'path_to_airline_logo.jpg'  # Add path to airline logo image
            }
            return render(request, 'airline_result.html', context)
    return redirect('some_default_view')  # Redirect to a default view if the request method is not POST

def booking(request):
    if request.method == 'POST':
        task_type = request.POST.get('task_type')

        if task_type == 'airline':

            from_city = request.POST.get('from_city')
            to_city = request.POST.get('to_city')
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            airline = request.POST.get('airline')
            layovers = request.POST.get('layovers')
            price = request.POST.get('price')
            message = request.POST.get('message')
            correct_result = request.POST.get('correct_result')
            task_type = request.POST.get('task_type')
            item_id = request.POST.get('item_id')
            
            request.session['from_city'] = request.POST.get('from_city')
            request.session['to_city'] = request.POST.get('to_city')
            request.session['from_date'] = request.POST.get('from_date')
            request.session['to_date'] = request.POST.get('to_date')
            request.session['airline'] = request.POST.get('airline')
            request.session['layovers'] = request.POST.get('layovers')
            request.session['price'] = request.POST.get('price')
            request.session['message'] = request.POST.get('message')
            request.session['correct_result'] = request.POST.get('correct_result')
            request.session['task_type'] = request.POST.get('task_type')
            request.session['item_id'] = request.POST.get('item_id')
        
        elif task_type=='hotel':
            from_city = request.POST.get('from_city')
            from_date = request.POST.get('from_date')
            to_date = request.POST.get('to_date')
            price = request.POST.get('price')
            no_of_rooms = request.POST.get('no_of_rooms')
            ratings=request.POST.get('ratings')
            message = request.POST.get('message')
            correct_result = request.POST.get('correct_result')
            task_type = request.POST.get('task_type')
            item_id = request.POST.get('item_id')
            
            request.session['from_city'] = request.POST.get('from_city')
            request.session['from_date'] = request.POST.get('from_date')
            request.session['to_date'] = request.POST.get('to_date')
            request.session['price'] = request.POST.get('price')
            request.session['no_of_rooms'] = request.POST.get('no_of_rooms')
            request.session['message'] = request.POST.get('message')
            request.session['ratings'] = request.POST.get('ratings')
            request.session['correct_result'] = request.POST.get('correct_result')
            request.session['task_type'] = request.POST.get('task_type')
            request.session['item_id'] = request.POST.get('item_id')
    
        print(f"TASKTYPe : {task_type},correct_result:{correct_result}",flush=True)
        

        return redirect('http://127.0.0.1:8000/bank_login/')


    return redirect('tasks')  # Redirect to a default view if the request method is not POST

def complete_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.time_end = int(time.time())


    print(f"reporeted : {request.session.get('reported')} ,task correcet : {repr(request.session.get('correct_result'))} ; {request.session.get('correct_result')} type : {type({request.session.get('correct_result')})}",flush=True)
    
    if request.session.get('reported'):
        print(f"SOOOOOOOO REPORTED",flush=True)
        item.status = 'reported'
    else:
        if request.session.get('correct_result') == 'True':
            item.status = 'completed'
        else:
            item.status = 'incorrect'
            item.message=request.session.get('message')
            messages.error(request, item.message)


    item.save()
    print(f"Task : {item.id} completed at {item.time_end}",flush=True)


    return redirect('tasks')
