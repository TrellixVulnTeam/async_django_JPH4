from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',  TemplateView.as_view(template_name='code_editor/code_editor.html'), name='code_editor_home'),
]
