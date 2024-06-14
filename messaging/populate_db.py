import os
import django
import random
import string
from django.conf import settings

# from django.contrib.auth.hashers import make_password

# # Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()
# print("Django settings module:", settings.CONFIGURED)  # Add this line to verify settings

from my_app.models import User 
from bank.models import BankUser

def generate_unique_user_id():
    while True:
        user_id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
        if not model.objects.filter(user_id=user_id).exists():
            return user_id

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

def populate_users(count):
    for _ in range(count):
        user_id = generate_unique_user_id(User)
        password = generate_password()

        BankUser.objects.create(user_id=user_id, password=password)
        User.objects.create(user_id=user_id)
        print(f'Successfully created User: {user_id}')

# def populate_bank_users(count):
#     for _ in range(count):
#         user_id = generate_unique_user_id(BankUser)
#         bank_user = BankUser.objects.create(user_id=user_id, password=make_password(password))
#         print(f'Successfully created BankUser: {user_id} with password: {password}')

def main():
    populate_users(10)
    # populate_bank_users(10)
    # print(generate_unique_user_id(),generate_password())

if __name__ == '__main__':
    main()
