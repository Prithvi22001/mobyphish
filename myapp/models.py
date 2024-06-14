from django.db import models
import time

def get_current_unix_timestamp():
    return int(time.time())

class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.user_id

class Item(models.Model):
    STATUS_CHOICES = [
        ('default', 'Default'),
        ('active', 'Active'),
        ('incorrect', 'Incorrect'),
        ('completed', 'Completed'),
        ('reported', 'Reported'),

    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)
    results=models.BinaryField()
    all_info=models.BinaryField()
    message=models.CharField(max_length=100)
    time_start = models.IntegerField(null=True, blank=True)
    time_end = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='default')

    def __str__(self):
        return self.task
