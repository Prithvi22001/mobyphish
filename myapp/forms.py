from django import forms

class UserIdForm(forms.Form):
    user_id = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100)
