from django import forms 
from fni_page.models import User_profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','password','email')
        widgets = {
            'username':forms.TextInput(attrs={'class':'form-control','placeholder': 'Enter your username'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
        }

class UserProfileInfoForm(forms.ModelForm):
    class Meta():
        model = User_profile 
        fields = ('occupation_and_monthly_saving',)
        widgets = {
            'occupation_and_monthly_saving':forms.Textarea(attrs={'class':'form-control'}),

        }