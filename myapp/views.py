from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import User, Item, ItemDump,Extension
from bank.models import BankUser,Transaction
from .forms import UserIdForm
import time
import urllib.parse
from . import task_generate
from django.conf import settings
import json
from django.http import JsonResponse
import ast
import pickle
import datetime
import random
import string
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
from django.urls import reverse
import os


logger = logging.getLogger('myapp')

def index(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphish.html', {'mail':mail,'fish': fish,'fish2':fish2 } )

def experiment(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphish-get-started.html', {'fish': fish,'fish2':fish2 } )

def study(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphishstudy.html', {'fish': fish,'fish2':fish2 } )

def about(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphisabout.html', {'mail':mail,'fish': fish,'fish2':fish2 } )

def extension(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphishextension.html', {'mail':mail,'fish': fish,'fish2':fish2 } )

def long_term(request):
    fish2=settings.MEDIA_URL+'fish2.png'
    fish=settings.MEDIA_URL+'fish.jpeg'
    mail=settings.MEDIA_URL+'mail1.png'

    return render(request,'mobyphishlongterm.html', {'mail':mail,'fish': fish,'fish2':fish2 } )



def login(request):
    if request.method == 'POST':
        form = UserIdForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']

            if User.objects.filter(user_id=user_id).exists() :
                user=User.objects.get(user_id=user_id)
                if user.check_password(password):
                    response = redirect('tasks')
                    response.set_cookie('user_id', user_id)
                    response.set_cookie('use_extension', user.use_extension)
                    response.set_cookie('long_term', user.long_term,max_age=60*60*24*365*2)
                    response.set_cookie('long_term_group', user.long_term_group,max_age=60*60*24*365*2)

                    logger.info(f"USER: {user_id} logged in and use_extension is set as {user.use_extension}")
                    return response
            else:
                logger.info(f"USER: {user_id} ,PASSWORD: {password} incorrect user ID or password ")
                form.add_error('user_id', 'Invalid user ID or password')
    else:
        form = UserIdForm()
    return render(request, 'home.html', {'form': form})

def logout_view(request):
    response = redirect('home')
    request.session.flush()
    preserve_cookies = ['long_term', 'long_term_group']

    for cookie in request.COOKIES:
        if cookie not in preserve_cookies :
            response.delete_cookie(cookie)
    return response

def generate_token(length=6):
    characters =  string.digits + string.ascii_letters
    token=''.join(random.choice(characters) for _ in range(length))
    return token

def generate_random_code(length=4):

    animals = ["Cat", "Dog", "Fox", "Bat", "Rat", "Cow", "Ant", "Bee", "Owl", "Hen", "Pig", "Ram", "Cub", "Yak", "Ape", "Bug", "Cod", "Elk", "Fly"]
    colors = ["Red", "Blu", "Grn", "Yel", "Org", "Pur", "Pnk", "Blk", "Wht", "Cyn", "Mag", "Lime", "Aqua", "Teal", "Gray", "Navy", "Gold", "Tan", "Mint", "Lav"]
    animal = random.choice(animals)
    color = random.choice(colors)
    number = random.randint(1, 99)
    username=[animal,color,str(number)]
    random.shuffle(username)
    return ''.join(username)
    # characters = string.ascii_letters + string.digits
    # return ''.join(random.choice(characters) for _ in range(length))

last_use_extension = False
long_term_group= 1

@csrf_exempt
def survey(request):
    global last_use_extension
    global long_term_group 

    if request.method== 'POST' :
        data= json.loads(request.body)
        logger.info(f"Got request from qualtrics creating userID and password")
        userID=""
        while True:
            userID=generate_random_code()
            if not User.objects.filter(user_id=userID).exists():
                break
        characters = string.ascii_lowercase + string.digits
        bank_password=''.join(random.choice(characters) for _ in range(4))
        
        # Alternate use_extension value
        use_extension = not last_use_extension
        last_use_extension = use_extension
        

        new_user=User(user_id=userID,password=bank_password,use_extension=use_extension,round_no=1,long_term=False,long_term_group=long_term_group)
        long_term_group= long_term_group+1 if long_term_group<3 else 1
        new_user.save()
        bank_user = BankUser(user_id=userID,password=bank_password)
        bank_user.save()
        logger.info(f"Created {userID} with PASSWORD: {bank_password} and use_extension: {use_extension}")
        return JsonResponse({'randomID':userID,'password':bank_password})



@csrf_exempt
def test_credentials(request):
    global last_use_extension
    global long_term_group 

    if request.method== 'GET' :
        # data= json.loads(request.body)
        logger.info(f"Got request from test_credentials creating userID and password")
        userID=""
        while True:
            userID=generate_random_code()
            if not User.objects.filter(user_id=userID).exists():
                break
        characters = string.ascii_lowercase + string.digits
        bank_password=''.join(random.choice(characters) for _ in range(4))
        
        # Alternate use_extension value
        use_extension = not last_use_extension
        last_use_extension = use_extension


        new_user=User(user_id=userID,password=bank_password,use_extension=use_extension,round_no=1,long_term=False,long_term_group=long_term_group)
        long_term_group= long_term_group+1 if long_term_group<3 else 1
        new_user.save()
        bank_user = BankUser(user_id=userID,password=bank_password)
        bank_user.save()
        logger.info(f"Created {userID} with PASSWORD: {bank_password} and use_extension: {use_extension}")
        return JsonResponse({'randomID':userID,'password':bank_password})


@csrf_exempt
def extension_download(request):

    if request.method== 'POST' :
        data= json.loads(request.body)
        logger.info(f"Got request from qualtrics to download extension")
        token=""
        while True:
            token=generate_token()
            if not Extension.objects.filter(token=token).exists():
                break
        
        temp=Extension(token=token)
        temp.save()
        return JsonResponse({'token':token})

@csrf_exempt
def download(request,token):
    extension = get_object_or_404(Extension, token=token)
    
    # Define the path to the ZIP file you want to download
    zip_file_path = os.path.join(settings.MEDIA_ROOT, 'PKI_CHROME.zip')
    
    if not os.path.exists(zip_file_path):
        raise Http404("ZIP file does not exist")
    
    # Open the file and return it as a response
    with open(zip_file_path, 'rb') as zip_file:
        response = HttpResponse(zip_file.read(), content_type='application/zip')
        response['Content-Disposition'] = f'attachment; filename={os.path.basename(zip_file_path)}'
        return response



def items_view(request):
    if 'user_id' not in request.COOKIES:
        return redirect('home')

    user_id = request.COOKIES['user_id']
    user = get_object_or_404(User, user_id=user_id)

    new_generated_tasks=False
    default_tasks_count = Item.objects.filter(user=user, status='default').count()
    complete_tasks_count = Item.objects.filter(user=user, status='completed').count()
    active_tasks_count = Item.objects.filter(user=user, status='active').count()
    reported_tasks_count = Item.objects.filter(user=user, status='reported').count()
    incorrect_tasks_count = Item.objects.filter(user=user, status='incorrect').count()
    
    total_correct_tasks=complete_tasks_count+active_tasks_count+incorrect_tasks_count
    logger.info(f"{user_id} Entering items_view function")



    # Generate tasks only if the number of default tasks is less than NO_OF_TASKS
    if default_tasks_count+complete_tasks_count+active_tasks_count< settings.NO_OF_TASKS:

        for _ in range(settings.NO_OF_TASKS):
            default_tasks_count = Item.objects.filter(user=user, status='default').count()
            if default_tasks_count+complete_tasks_count +active_tasks_count+reported_tasks_count< settings.NO_OF_TASKS:
                ans=task_generate.generate_task()
                task=Item(user=user,task=ans['task'],results=pickle.dumps(ans['results']),all_info=pickle.dumps(ans),status='default')
                task.save()
                new_generated_tasks=True
                
    if default_tasks_count+active_tasks_count==0:
        if user.round_no == 1:
            user.round_no = 2
            user.use_extension= not user.use_extension
            user.save()
            logger.info(f"USER: {user_id} completed round 1")
            items = Item.objects.filter(user=user)
            for item in items:
                ItemDump.objects.create(
                    user=item.user,
                    task=item.task,
                    results=item.results,
                    all_info=item.all_info,
                    message=item.message,
                    time_start=item.time_start,
                    time_end=item.time_end,
                    bank_vist=item.bank_vist,
                    status=item.status,
                    phish=item.phish,
                    result=item.result
                )
            items.delete()
            message = 'Round completed. Proceed to the next round.'
            request.session.flush()

            url = reverse('home') + f'?message={message}'
            response = redirect(url)
            for cookie in request.COOKIES:
                preserve_cookies = ['long_term', 'long_term_group']
                if cookie not in preserve_cookies :
                    response.delete_cookie(cookie)
            return response

        elif default_tasks_count+active_tasks_count==0 and user.round_no == 2:
            logger.info(f"USER: {user_id} both round completed")
            items = Item.objects.filter(user=user)
            for item in items:
                ItemDump.objects.create(
                    user=item.user,
                    task=item.task,
                    results=item.results,
                    all_info=item.all_info,
                    message=item.message,
                    time_start=item.time_start,
                    time_end=item.time_end,
                    bank_vist=item.bank_vist,
                    status=item.status,
                    phish=item.phish,
                    result=item.result
                )
            items.delete()

            # response = redirect('tasks')
            user.round_no += 1 
            user.use_extension=True
            user.long_term=True
            long_term_group=user.long_term_group
            user.save()
            user_id = request.COOKIES['user_id']
            response = render(request, 'items.html', {'items': '', 'completed': "YES"})
            # for cookie in request.COOKIES:
            #     response.delete_cookie(cookie)
            
            response.set_cookie('user_id', user_id)
            response.set_cookie('use_extension', True )
            response.set_cookie('long_term', True ,max_age=60*60*24*365*2)
            response.set_cookie('long_term_group', long_term_group,max_age=60*60*24*365*2 )
            # return render(request, 'items.html', {'items': '','completed':"YES"})
            return response

    items = Item.objects.filter(user=user)
    active_item = items.filter(status='active').first()

    if new_generated_tasks:
        default_items = items.filter(status='default')
        item_count = default_items.count()
        phish_count = item_count // 5  # 20% of items
        phish_items = random.sample(list(default_items), phish_count)
        
        url_attack_count = (2 * phish_count) // 3
        cert_attack_count = phish_count - url_attack_count
        url_attack_items = random.sample(phish_items, url_attack_count)
        cert_attack_items = [item for item in phish_items if item not in url_attack_items]

        for item in url_attack_items:
            if not item.phish:
                item.phish = True
                item.phish_type = 'url'
                item.save()

        for item in cert_attack_items:
            if not item.phish:
                item.phish = True
                item.phish_type = 'cert'
                item.save()

    # Order items by status
    status_order = ['active', 'default', 'completed', 'reported', 'incorrect']
    ordered_items = sorted(items, key=lambda x: status_order.index(x.status))


    return render(request, 'items.html', {'items': ordered_items, 'active': active_item.id if active_item else None})

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
            logger.info(f"USER : {user_id}, ITEM ID: {item_id} active item clicked again")
            request.session['phish'] = item.phish
            request.session['phish_type'] = item.phish_type
            request.session['item_id'] = item_id 
            # request.session.modified = True
            request.session.save()  # Explicitly save the session

            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this item is phished {item.phish}")
            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this sission{request.session.items()}")

            return redirect('results',item_id=item_id)
        else:
            logger.info(f"USER: {user_id},ITEM ID: {item_id} not active clicked")
            messages.error(request, "Cannot start this task until the active highlighted task is completed.")
            return redirect('tasks')  # Redirect back to items page

    else:
        if item.status=='active':
            logger.info(f"USER: {user_id}, ITEM ID: {item_id} active item clicked ")
            request.session['phish'] = item.phish
            request.session['phish_type'] = item.phish_type
            request.session['item_id'] = item_id 
            # request.session.modified = True
            request.session.save()  # Explicitly save the session

            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this item is phished {item.phish}")
            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this sission{request.session.items()}")

            return redirect('results',item_id=item_id)

        else:
            item.time_start = int(time.time())
            item.status = 'active'
            item.all_info=item.all_info
            item.save()
            request.session['phish'] = item.phish
            request.session['phish_type'] = item.phish_type
            request.session['item_id'] = item_id 
            # request.session.modified = True
            request.session.save()  # Explicitly save the session

            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this item is phished {item.phish}")
            logger.info(f"USER: {user_id} ,ITEM ID: {item_id} started at {item.time_start} this sission{request.session.items()}")

            return redirect('results', item_id=item.id)


def results(request, item_id):

    item = get_object_or_404(Item, id=item_id)
    all_info=pickle.loads(item.all_info)

    search_results=all_info['results']
    random.shuffle(search_results)

    task=all_info['task']
    task_type = all_info['type']  # Get the type of task

    return render(request, 'results.html', {'task': task, 'task_id': item_id,'search_results':search_results, 'task_type': task_type})

def travel_page(request, item_id):
    if request.method == 'POST':
        user_id = request.COOKIES['user_id']
        task_type = request.POST.get('task_type')

        if task_type == 'hotel':
            from_city = request.POST.get('from_city')
            from_date = request.POST.get('from_date').split(',')[0]
            to_date = request.POST.get('to_date').split(',')[0]
            price = request.POST.get('price')
            ratings=request.POST.get('rating')
            no_of_rooms = request.POST.get('no_of_rooms')
            correct_result = request.POST.get('correct_result') 
            hotel_snippet_short = request.POST.get('hotel_snippet_short') 
            hotel_snippet = request.POST.get('hotel_snippet') 
            message = request.POST.get('message')
            task_type = request.POST.get('task_type')
            hotel=request.POST.get('hotel')
            hotel_image=request.POST.get('hotel_image')

            logger.info(f"USER: {user_id} selected RESULT:{correct_result} for {task_type} task")


            request.session['from_city'] = request.POST.get('from_city')
            request.session['from_date'] = request.POST.get('from_date')
            request.session['to_date'] = request.POST.get('to_date')
            request.session['price'] = request.POST.get('price')
            request.session['ratings'] = request.POST.get('ratings')
            request.session['no_of_rooms'] = request.POST.get('no_of_rooms')
            request.session['correct_result'] = request.POST.get('correct_result')
            request.session['message'] = request.POST.get('message')
            request.session['task_type'] = request.POST.get('task_type')
            request.session['hotel'] = request.POST.get('hotel')
            request.session['hotel_image'] = request.POST.get('hotel_image')
            request.session['item_id'] = item_id

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
                'hotel_snippet_short':hotel_snippet_short,
                'hotel_snippet':hotel_snippet,
                'hotel':hotel,
                'blurb': "Experience the best stay at our luxurious hotel.",
                'blurb1': "Comfortable and well-furnished rooms available.",
                'hotel_image': hotel_image, 
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
            airline_logo= request.POST.get('airline_logo') #settings.MEDIA_URL+airline+'.png'

            logger.info(f"USER: {user_id} selected RESULT:{correct_result} for {task_type} task")

            request.session['from_city'] = request.POST.get('from_city')
            request.session['to_city'] = request.POST.get('to_city')
            request.session['from_date'] = request.POST.get('from_date')
            request.session['to_date'] = request.POST.get('to_date')
            request.session['airline'] = request.POST.get('airline')
            request.session['price'] = request.POST.get('price')
            request.session['message'] = request.POST.get('message')
            request.session['layovers'] = request.POST.get('layovers')
            request.session['correct_result'] = request.POST.get('correct_result')
            request.session['task_type'] = request.POST.get('task_type')
            request.session['airline_logo'] = request.POST.get('airline_logo')
            request.session['item_id'] = item_id


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
                'airline_logo': airline_logo  # Add path to airline logo image
            }
            return render(request, 'airline_result.html', context)
    return redirect('tasks')

def booking(request):
    if request.method == 'POST':
        task_type = request.POST.get('task_type')
        user_id = request.COOKIES['user_id']
        item_id=request.session.get('item_id')

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
            
        phish = request.session.get('phish', None)  # Default to None to see if it is missing
        phish_type = request.session.get('phish_type', None)  # Default to None to see if it is missing

        logger.info(f"USER: {user_id}, ITEM: {item_id}, making URL because phish={phish} and phish_type={phish_type}")

        # Check if phish is None and log it
        if phish is None:
            logger.error(f"USER: {user_id}, ITEM: {item_id}, phish is None. Session: {request.session.items()}")

        item = get_object_or_404(Item, id=item_id)
        item.bank_vist = int(time.time())
        item.save()

        ###TODO PHISHING ATTACKS
        good_url='acct.ilogicalLoansSavings'            
        letters = string.ascii_lowercase
        pre=''.join(random.choice(letters) for i in range(3))

        if phish:
            bad_urls=['acct-ilogicalLoansSavings','acct.ilogical.LoansSavings','acct.iIogicalLoansSavings','acct.llogicalLoansSavings','acct.ilogicalLoanSavings','acct.ilogicaILoansSavings','acct.lIogicalLoansSavings']
            bad_prefix=['wcwm','wzho']
            url=''
            if phish_type=='cert':
                logger.info(f"USER: {user_id}, ITEM: {item_id} ,phish_type:{phish_type} so ,cert attack")
                url='https://'+random.choice(bad_prefix)+'.'+good_url+'.mobyphish.com/bank_login'
            else:
                logger.info(f"USER: {user_id}, ITEM: {item_id} ,phish_type:{phish_type} so ,url attack")
                url='https://'+'w'+pre+'.'+random.choice(bad_urls)+'.mobyphish.com/bank_login'
        else:
            logger.info(f"USER: {user_id}, ITEM: {item_id} no attack")
            url='https://'+'w'+pre+'.'+good_url+'.mobyphish.com/bank_login'
        logger.info(f"USER: {user_id}, ITEM: {item_id} redirecting to {url}")



        if settings.DEBUG:
            #if DEBUG is TRUE do not rediret to phishing sites
            return redirect('bank_login')
        else:
            return redirect(url)


    return redirect('tasks')  # Redirect to a default view if the request method is not POST

def complete_item(request, item_id):
    user_id = request.COOKIES['user_id']
    item = get_object_or_404(Item, id=item_id)
    item.time_end = int(time.time())
    # trans=Transaction.objects.get(user_id=request.COOKIES['user_id'],task_id=item_id)
    
    if request.session.get('reported'):
        if request.session.get('phish'):
            logger.info(f"USER: {user_id} ITEM: {item_id} was reported and is phished {request.session.get('phish')}")
            item.result='sucess'
        else:
            logger.info(f"USER: {user_id} ITEM: {item_id} was reported and is phished {request.session.get('phish')}")
            item.result='fail'

        item.status = 'reported'

    else:
        if request.session.get('correct_result') == 'True':
            if request.session.get('phish'):
                logger.info(f"USER: {user_id} ITEM: {item_id} was not reported and is phished {request.session.get('phish')}")
                item.result='fail'
            else:
                logger.info(f"USER: {user_id} ITEM: {item_id} was not reported and is phished {request.session.get('phish')}")
                item.result='sucess'
            item.status = 'completed'
        else:
            item.status = 'incorrect'
            logger.info(f"USER: {user_id} ITEM: {item_id} was not reported,incorrect and is phished {request.session.get('phish')}")
            item.result='fail'
            item.message=request.session.get('message')
            messages.error(request, item.message)
    


    item.save()
    logger.info(f"USER: {user_id} ITEM: {item_id} completed at {item.time_end}")
    request.session.flush()
    logger.info(f"USER: {user_id} flush session {request.session.keys()}")

    return redirect('tasks')


def report(request):
    try:
        user_id = request.COOKIES['user_id']
        item_id=request.session.get('item_id')
        item = get_object_or_404(Item, id=item_id)
        item.status = 'default'
        item.save()
        logger.warning(f'USER: {user_id} reported task {item_id} on non bank page resetting to default')
    except Exception as e:
        logger.error(f"IN REPORT {str(e)}")

    return redirect('tasks')