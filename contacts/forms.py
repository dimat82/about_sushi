from django import forms
from contacts.models import Feedback
from django.contrib.auth.models import User

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['name','email','phone','content']


class FormRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email','first_name','last_name']


class LoginForm(forms.Form):
    username = forms.CharField(label='имя')
    password = forms.CharField(widget=forms.PasswordInput,label='пароль')

