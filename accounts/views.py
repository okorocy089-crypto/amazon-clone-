from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import User, CardForm
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout, get_user_model 
from catalog.models import Category, Product
from cart.views import merge_guest_cart_into_user
from django.contrib.auth.decorators import login_required


def homepage_view(request):

    def get_section(name_fragment):
        cat = Category.objects.filter(name__icontains=name_fragment).first()
        if cat:
            return {
                "id": cat.id,
                "products": Product.objects.filter(category=cat)[:4],
            }
        return {"id": None, "products": []}

    sections = {
        "fashion":   get_section("clothing"),
        "cutlery":   get_section("cutlery"),
        "computers": get_section("computer"),
        "sports":    get_section("sport"),
        "music":     get_section("musical"),
        "pets":      get_section("pet"),
        "mobile":    get_section("mobile"),
        "wears":     get_section("wear"),
        "tech":      get_section("dope"),
        "school":    get_section("school"),
        "gaming":    get_section("gaming"),
        "toys":      get_section("toy"),
    }

    return render(request, "homepage.html", {"sections": sections})

def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            request.session["registration_data"] = {
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "email": form.cleaned_data["email"],
                "password": form.cleaned_data["password"],
            }
            return redirect("security_question")
    else:
        form = RegistrationForm()

    return render(request, "accounts/register.html", {"form": form})


def security_question_view(request):
    registration_data = request.session.get("registration_data")

    
    if not registration_data:
        return redirect("register")

    if request.method == "POST":
        question = request.POST.get("security_question")
        answer = request.POST.get("security_answer")

        if not question or not answer:
            return render(request, "accounts/security_question.html", {
                "questions": User.SECURITY_QUESTIONS,
                "error": "Please choose a question and provide an answer.",
            })

        user = User.objects.create_user(
            email=registration_data["email"],
            password=registration_data["password"],
            first_name=registration_data["first_name"],
            last_name=registration_data["last_name"],
            security_question=question,
            security_answer=answer,
        )

        del request.session["registration_data"]  

        login(request, user) 
        merge_guest_cart_into_user(request, user)
        return redirect("homepage")

    return render(request, "accounts/security_question.html", {
        "questions": User.SECURITY_QUESTIONS,
    })


def login_view(request):
    error = None

    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        if not email or not password:
            error = "Field required"
        else:
            user = authenticate(request, username=email, password=password)
            if user is None:
                error = "Incorrect email or password"
            else:
                auth_login(request, user)
                merge_guest_cart_into_user(request, user)
                return redirect("homepage")

    return render(request, "accounts/login.html", {"error": error})


User = get_user_model()

def password_reset_email_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        try:
            user = User.objects.get(email=email)
            request.session["reset_email"] = email
            return redirect("password_reset_question")
        except User.DoesNotExist:
            return render(request, "accounts/password_reset_email.html", {
                "error": "Email does not exist"
            })
    return render(request, "accounts/password_reset_email.html")


def password_reset_question_view(request):
    reset_email = request.session.get("reset_email")
    if not reset_email:
        return redirect("password_reset_email")

    user = User.objects.get(email=reset_email)
    question_label = user.get_security_question_display()

    if request.method == "POST":
        answer = request.POST.get("security_answer", "").strip().lower()
        if answer == user.security_answer.strip().lower():
            request.session["reset_verified"] = True
            return redirect("password_reset_new")
        else:
            return render(request, "accounts/password_reset_question.html", {
                "question_label": question_label,
                "error": "Incorrect answer"
            })

    return render(request, "accounts/password_reset_question.html", {
        "question_label": question_label
    })


def password_reset_new_view(request):
    if not request.session.get("reset_verified"):
        return redirect("password_reset_email")

    if request.method == "POST":
        password1 = request.POST.get("new_password")
        password2 = request.POST.get("confirm_password")

    if not password1 or not password2:
        return render(request, "accounts/password_reset_new.html", {"error": "Field required"})

    if len(password1) < 8:
        return render(request, "accounts/password_reset_new.html", {
            "error": "Password must be at least 8 characters"
        })
    if password1 != password2:
        return render(request, "accounts/password_reset_new.html", {
            "error": "Passwords do not match"
        })

    reset_email = request.session.get("reset_email")
    user = User.objects.get(email=reset_email)
    user.set_password(password1)
    user.save()

    request.session.pop("reset_email", None)
    request.session.pop("reset_verified", None)

    return redirect("login")
 
    return render(request, "accounts/password_reset_new.html")


def logout_view(request):
    auth_logout(request)
    return redirect("homepage")

@login_required
def add_card(request):
    existing_card = getattr(request.user, "paymentcard", None)

    if request.method == "POST":
        form = CardForm(request.POST, instance=existing_card)
        if form.is_valid():
            card = form.save(commit=False)
            card.user = request.user
            card.save()
            return redirect("checkout")
    else:
        form = CardForm(instance=existing_card)

    return render(request, "accounts/add_card.html", {"form": form})


def unlink_card(request):
    if hasattr(request.user, 'paymentcard'):
        request.user.paymentcard.delete()
    return redirect("homepage")

def delete_account_view(request):
    return render(request, "accounts/delete_account.html")

def confirm_delete_view(request):
    if request.method == "POST":
        request.user.delete()
        return redirect("homepage")
    return redirect("delete_account")


