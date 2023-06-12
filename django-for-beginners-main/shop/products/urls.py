from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('buy/', views.buy, name='buy'),
    path('buy/register/', views.register, name='register'),
    path('buy/login/', views.login, name='login'),
    path('buy/logout/', views.logout, name='logout'),
]
