from django import forms
from django.contrib.auth import get_user_model
from .models import PaymentCard

User = get_user_model()

class RegistrationForm(forms.Form):
    first_name = forms.CharField(max_length=150)
    last_name = forms.CharField(max_length=150)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Email required")
        return email

    def clean_password(self):
        password = self.cleaned_data.get("password")
        if len(password) < 8:
            raise forms.ValidationError("Password must be 8 characters or more")
        return password

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error("confirm_password", "Passwords don't match")

        return cleaned_data

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email.endswith("@gmail.com"):
            raise forms.ValidationError("Email required")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists")
        return email
    