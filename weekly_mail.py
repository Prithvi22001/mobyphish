import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'messaging.settings')  # Replace with your actual project name
django.setup()

# Step 2: Import the SecureData model
from myapp.models import UserData  # Replace 'your_app_name' with the actual app name

# Step 3: Query all data
all_secure_data = UserData.objects.all()

# Step 4: Access the data and print it
for data in all_secure_data:
    print(f"Name: {data.name}, Encrypted Value: {data.email}")
