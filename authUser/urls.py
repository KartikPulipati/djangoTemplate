from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signUp, name='signup'),
    path('email_verification/', views.emailVer, name='emailVer'),
]