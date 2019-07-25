from django.contrib import admin
from django.urls import path

from zitalkapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.auth_login), 
    path('logout', views.auth_logout), 
    path('signup', views.signup), 
]
