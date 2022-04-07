from importlib.resources import path
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path

from .views import (
   donationPage
)

urlpatterns = [
    path('',  donationPage, name='donation_home'),
]
