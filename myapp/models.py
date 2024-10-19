from django.db import models
import time
from django_cryptography.fields import encrypt

def get_current_unix_timestamp():
    return int(time.time())

class UserData(models.Model):
    user_id=models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    name = encrypt(models.CharField(max_length=255)) 
    email = encrypt(models.CharField(max_length=255)) 
    def __str__(self):
        return self.user_id

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    password=models.CharField(max_length=100)
    round_no=models.IntegerField(null=True, blank=True)
    use_extension=models.BooleanField(default=False)
    long_term=models.BooleanField(default=False)
    long_term_group=models.IntegerField(null=True, blank=True)
    
    def check_password(self, raw_password):
        return raw_password==self.password

    def __str__(self):
        return self.user_id

class Extension(models.Model):
    token=models.CharField(max_length=10,unique=True)


class Item(models.Model):
    STATUS_CHOICES = [
        ('test', 'Test'),        
        ('default', 'Default'),
        ('active', 'Active'),
        ('incorrect', 'Incorrect'),
        ('completed', 'Completed'),
        ('reported', 'Reported'),
    ]

    RESULT_CHOICES= [
        ('fail', 'Fail'),
        ('sucess', 'Sucess'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=1000)
    results=models.BinaryField()
    all_info=models.BinaryField()
    message=models.CharField(max_length=1000)
    time_start = models.IntegerField(null=True, blank=True)
    time_end = models.IntegerField(null=True, blank=True)
    bank_vist=models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=100, choices=STATUS_CHOICES, default='default')
    phish = models.BooleanField(default=False)
    phish_type = models.CharField(null=True,default='',max_length=10)
    result= models.CharField(max_length=100, choices=RESULT_CHOICES, default='')
    round_no=models.IntegerField(null=True, blank=True)


    def __str__(self):
        return self.task

class ItemDump(models.Model):
    STATUS_CHOICES = [
        ('default', 'Default'),
        ('active', 'Active'),
        ('incorrect', 'Incorrect'),
        ('completed', 'Completed'),
        ('reported', 'Reported'),
    ]

    RESULT_CHOICES= [
        ('fail', 'Fail'),
        ('sucess', 'Sucess'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    results=models.BinaryField()
    all_info=models.BinaryField()
    message=models.CharField(max_length=100)
    time_start = models.IntegerField(null=True, blank=True)
    time_end = models.IntegerField(null=True, blank=True)
    bank_vist=models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='default')
    phish = models.BooleanField(default=False)
    phish_type = models.CharField(null=True,default='url',max_length=10)
    result= models.CharField(max_length=10, choices=RESULT_CHOICES, default='sucess')
    round_no=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.task


class BlockedUser(models.Model):

    user_id = models.CharField(max_length=255, unique=True)  # Ensure uniqueness
    def __str__(self):
        return self.user_id
    
