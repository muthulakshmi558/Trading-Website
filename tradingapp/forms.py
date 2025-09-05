# tradingapp/forms.py
from django import forms
from .models import Subscriber
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import PartnerRequest
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
        widgets = {
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Your Email',
                'class': 'px-3 py-2 rounded-l-md w-full text-black'
            })
        }




from django import forms
from .models import PartnerRequest

class PartnerRequestForm(forms.ModelForm):
    class Meta:
        model = PartnerRequest
        fields = ["name", "phone", "email", "city", "pincode"]
        widgets = {
            "name": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter your name"
            }),
            "phone": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter mobile number"
            }),
            "email": forms.EmailInput(attrs={
                "class": "form-control",
                "placeholder": "Enter email address"
            }),
            "city": forms.Select(attrs={
                "class": "form-select",
            }),
            "pincode": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Enter pincode"
            }),
        }

# Signup Form
class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=100, required=True, label="Name")
    mobile = forms.CharField(max_length=15, required=True, label="Mobile No")
    email = forms.EmailField(required=True, label="E-mail Id")

    class Meta:
        model = User
        fields = ("username", "name", "mobile", "email", "password1", "password2")

    def clean_mobile(self):
        mobile = self.cleaned_data.get("mobile")
        if not mobile.isdigit():
            raise forms.ValidationError("Mobile number should contain only digits.")
        if len(mobile) < 10:
            raise forms.ValidationError("Mobile number should be at least 10 digits.")
        return mobile

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Enter Username"
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            "class": "form-control custom-input",
            "placeholder": "Enter Password"
        })
    )