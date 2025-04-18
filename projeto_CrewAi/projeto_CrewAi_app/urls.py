from django.contrib import admin
from django.urls import include, path
from .views import *


urlpatterns = [
    path('', home_view, name='home'),  
    path('exemplo/', exemplo_view, name='exemplo'),  
]
