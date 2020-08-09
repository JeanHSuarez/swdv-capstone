from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Employee, Member
from django.core.exceptions import ValidationError

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['image']

#Creating Member

class MemberRegistrationForm(forms.Form):
    ssn = forms.CharField(label='Enter Social Security Number: ', min_length=10, max_length=10)
    firstName = forms.CharField(label='Enter First Name', min_length=0, max_length=150)
    middleName = forms.CharField(label='Enter Middle Name', min_length=0, max_length=150)
    lastName = forms.CharField(label='Enter Last Name', min_length=0, max_length=150)
    diagnosis = forms.CharField(label='Enter Diagnosis', min_length=0, max_length=150)

    


class MemberUpdateForm(forms.ModelForm):
    ssn = forms.CharField()

    class Meta:
        model = Member
        fields = ['firstName', 'middleName', 'lastName', 'diagnosis', 'intakeDate']




"""

    def clean_ssn(self):
        ssn = self.cleaned_data['ssn']
        r = Member.objects.filter(ssn=ssn)
        if r.count():
            raise  ValidationError("SSN already exists")
        return ssn

    def clean_firstName(self):
        firstName = self.cleaned_data['firstName']
        return firstName

    def clean_middleName(self):
        middleName = self.cleaned_data['middleName']
        return middleName

    def clean_lastName(self):
        lastName = self.cleaned_data['lastName']
        return lastName



class CustomUserCreationForm(forms.Form):
    username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
    email = forms.EmailField(label='Enter email')
    password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        r = User.objects.filter(username=username)
        if r.count():
            raise  ValidationError("Username already exists")
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        r = User.objects.filter(email=email)
        if r.count():
            raise  ValidationError("Email already exists")
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise ValidationError("Password don't match")

        return password2

    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1']
        )
        return user
"""

