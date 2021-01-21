from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Customer

class ExtendedUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def clean(self):
        email = self.cleaned_data.get('email')
        username = self.cleaned_data.get('username')
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username already exists")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        if password1!=password2:
            raise forms.ValidationError("Passwords did not match")
        return self.cleaned_data

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def save(self, commit = True):
        user = super().save(commit=False)

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
        return user

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('organisation', 'employee_id', 'mobile_number', 'id_card')