from django.urls import path
from . import views

urlpatterns = [
   path('', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('upload/', views.upload, name='upload'),
   path('find/', views.find, name='find'),
   path('comp/', views.comp, name='comp'),
]