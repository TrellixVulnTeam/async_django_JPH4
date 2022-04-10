from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import (
    Donate,
    Charge,
    ProductView,
    CreateIntent


)

urlpatterns = [
    path('create-payment-intent/', CreateIntent.as_view(), name='create-payment-intent'),
    path('donate/', Donate, name='donate'),
    path('product/', ProductView, name='product'),
    path('ceckout/', Charge, name='charge'),

]
