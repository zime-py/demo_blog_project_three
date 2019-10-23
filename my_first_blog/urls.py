from django.contrib import admin
from django.urls import path, include
from django.conf import settings # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
]

if settings.DEBUG: # new
    #urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
