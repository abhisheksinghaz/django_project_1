from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1','password2']


# the following class will allow to update the username and email
class UserUpdatedForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


# the following class will allow to update the profile image
class ProfileUpdatedForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']