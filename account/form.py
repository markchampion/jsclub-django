from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from account.models import Account


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True, widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = Account
        fields = ['firstname', 'lastname', 'phone', 'room', 'dob']