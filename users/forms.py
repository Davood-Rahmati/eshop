from django import forms
from .models import User


class UserRegistrationForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()


class UserLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class UserCreateForm(forms.Form):
    full_name = forms.CharField()
    mobile = forms.CharField()
    date_of_birth = forms.DateTimeField()
    national_code = forms.IntegerField()
    email = forms.EmailField()
    sheba_bank = forms.CharField()
    address_1 = forms.CharField()
    address_2 = forms.CharField()
    address_3 = forms.CharField()
    message = forms.CharField()

class UserUpdateForm(forms.ModelForm):
    class meta:
        model = User
        field = ('full_name','mobile','date_of_birth','national_code', 'email', 'sheba_bank', 'address_1', 'address_2', 'address_3' , 'message')