from django.urls import path
from .views import *
urlpatterns = [
    path('post/add/', post_add, name='post_add'),
    path('account/info', account_info, name='account_info'),
    path('reset_password', change_password, name='change_password'),
    path('register', register, name='register'),
]

