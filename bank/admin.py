from django.contrib import admin
from .models import BankUser, Transaction

admin.site.register(BankUser)
admin.site.register(Transaction)
