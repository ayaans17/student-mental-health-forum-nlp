from django.urls import path
from . import views
from .models import Forums

urlpatterns = [
    path('', views.hi2, name='homepage'),
    path('index', views.hi,name='home'),
    path('login', views.hi3,name='login'),
    path('likes', views.likes,name='likes'),
    path('logout', views.logout,name='logout'),
    path('forums', views.forums,name='forums'),
    path('template', views.template,name='template'),
]