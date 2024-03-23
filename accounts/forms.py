from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from accounts.models import Team, Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, label='Username')
    password = forms.CharField(max_length=100, label='Password', widget=forms.PasswordInput)
    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError('Username or Password is Wrong, Please Try Again!')
        return super(LoginForm, self).clean()

class SignupForm(UserCreationForm):
    team = forms.CharField(show_hidden_initial='true', required=True)
    class Meta:
        model = User
        fields = ['username', 'team', 'password1', 'password2']
