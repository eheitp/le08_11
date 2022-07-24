from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

from compte import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import auth_login


app_name = 'compte'

urlpatterns = [
    path('register/', views.log,name='reg'),

]