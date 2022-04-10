from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',  include('allauth.urls')),
    path('',  TemplateView.as_view(template_name='home/index.html'), name='home'),
    path('playground/', include('home.urls')),
    path('pokedex/', include('pokedex.urls')),
    path('code-editor/', include('code_editor.urls')),
    path('blog/', include('blog.urls')),
    # path('store/', include('ecommerce.urls')),
    path('api/blog/', include('blog_api.urls')),
    path('todo/', include('todo.urls')),
    path('api/todo/', include('todo_api.urls')),
    path('chat/', include('chat.urls')),
    path('stripe-testing/', include('stripe_testing.urls')),
]
