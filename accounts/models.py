from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
import uuid
from django import forms

# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)  # hashes the password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None

    SECURITY_QUESTIONS = [
        ('color', 'What is your favorite color?'),
        ('month', 'What month is your birthday?'),
        ('hobby', 'What is your hobby?'),
        ('food', 'What is your favorite food?'),
        ('club', 'What sports club are you a fan of?'),
    ]
    email = models.EmailField(unique=True)
    security_question = models.CharField(max_length=50, choices=SECURITY_QUESTIONS, default='color')
    security_answer = models.CharField(max_length=255)


    USERNAME_FIELD = "email"   
    REQUIRED_FIELDS = []  

    objects = CustomUserManager() 

    def __str__(self):
        return self.email



class PaymentCard(models.Model):
    ISSUER_CHOICES = [
        ("visa", "Visa"),
        ("mastercard", "MasterCard"),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    issuer_type = models.CharField(max_length=20, choices=ISSUER_CHOICES)
    cardholder_name = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16, unique=True)
    expiry = models.CharField(max_length=5)  # format: MM/YY
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.get_issuer_type_display()} card for {self.user.email}"

class CardForm(forms.ModelForm):
    class Meta:
        model = PaymentCard
        fields = ['issuer_type', 'cardholder_name', 'card_number', 'expiry', 'cvv']
        widgets = {
            'card_number': forms.PasswordInput(attrs={'placeholder': '1234 5678 9012 3456'}),
            'cvv': forms.PasswordInput(attrs={'placeholder': '123'}),
            'expiry': forms.TextInput(attrs={'placeholder': 'MM/YY'}),
        }
    

