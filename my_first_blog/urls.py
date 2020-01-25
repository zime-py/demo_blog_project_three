from django.contrib import admin
from django.urls import path, include #, re_path
from django.conf import settings # new
from django.conf.urls.static import static # new
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
#from forum.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('blog.urls')),
    path('cadmin/', include('cadmin.urls')),
    #path('kk', indexa))
    path('accounts/password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
 
    path('accounts/reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
 
    path('accounts/reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),

]

if settings.DEBUG: # new
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
