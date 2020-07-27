from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('base/', views.base, name='child'),
    path('child/', views.child, name='child')
]