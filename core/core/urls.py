from django.contrib import admin
from django.urls import path
from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api/', urls),
]
