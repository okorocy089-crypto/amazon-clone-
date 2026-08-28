from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register_view, name="register"),
    path("security-question/", views.security_question_view, name="security_question"),
    path("", views.homepage_view, name="homepage"),
    path("login/", views.login_view, name="login"),
    path("password-reset/", views.password_reset_email_view, name="password_reset_email"),
    path("password-reset/question/", views.password_reset_question_view, name="password_reset_question"),
    path("password-reset/new/", views.password_reset_new_view, name="password_reset_new"),
    path("logout/", views.logout_view, name="logout"),
    path("add-card/", views.add_card, name="add_card"),
    path("unlink-card/", views.unlink_card, name="unlink_card"),
    path("delete-account/", views.delete_account_view, name="delete_account"),
    path("confirm-delete/", views.confirm_delete_view, name="confirm_delete"),
]
