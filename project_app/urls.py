from django.urls import path
from . import views
from .views import LoginView, Register

app_name = 'project_app'

urlpatterns = [
    path('register', Register.as_view()),
    path('login', LoginView.as_view()),


]
