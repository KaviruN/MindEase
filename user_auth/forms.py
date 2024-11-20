from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile
class SignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your First Name'
    }))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your Last Name'
    }))
    email = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'Enter your email'
    }))
    username = forms.CharField(max_length=10, required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Enter your Username'
    }))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter your Password'
    }))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm your Password'
    }))
    birthday = forms.DateField(required=True, widget=forms.PasswordInput(attrs={
        'type': 'date'
    }))
    gender = forms.ChoiceField(choices=[('M', 'Male'), ('F', 'Female')], required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'password1', 'password2', 'birthday', 'gender')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.save()
        UserProfile.objects.create(
            user=user,
            birthday=self.cleaned_data['birthday'],
            gender=self.cleaned_data['gender']
        )
        return user