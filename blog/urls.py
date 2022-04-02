from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from .views import blogDetail

urlpatterns = [
    path('',  TemplateView.as_view(template_name='blog/index.html'), name='blog_home'),
    path('detail/<int:pk>/',  blogDetail.as_view(), name='blog_detail'),
]
