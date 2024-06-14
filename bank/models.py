from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password, check_password

class BankUser(models.Model):
    user_id = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # Store hashed password

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

    def check_password(self, raw_password):
        return raw_password==self.password

    def __str__(self):
        return self.user_id

class Transaction(models.Model):
    user = models.ForeignKey(BankUser, related_name='transactions', on_delete=models.CASCADE)
    to = models.CharField(max_length=100)
    task_id=models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    time_paid = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Transaction from {self.user.user_id} to {self.to} - Amount: {self.amount}"
