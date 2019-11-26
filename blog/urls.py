from django.urls import path
from blog.views import *
urlpatterns = [
    path('', post_list, name='post_list'),
    path('detail/<int:id>', post_detail, name='detail'),
    path('category/<name>', post_by_category, name='category'),
    path('contact/', contact, name = 'contact'),
    #path('track_user/', track_user, name = 'track_user'),

    path('login/', login, name = 'blog_login'),   
    path('logout/', logout, name = 'blog_logout'),
    path('admin_page/', admin_page, name = 'admin_page'),
    path('me/', me, name = 'me'),
]