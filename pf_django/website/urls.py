from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth import views as auth_views


urlpatterns = [
   path('', views.login, name='login'),
   path('home/', views.home, name='home'),
   path('upload/', views.upload, name='upload'),
   path('find/', views.find, name='find'),
   path('comp/', views.comp, name='comp'),
   path('contactus/', views.contactus, name='contactus'),
   path('ourmoto/', views.ourmoto, name='ourmoto'),
   path('logout/',auth_views.LogoutView.as_view(),name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

"""path('', views.login, name='login'),"""