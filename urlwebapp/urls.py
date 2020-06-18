
from django.contrib import admin
from django.urls import path,include
from shortener import views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("shortener.urls"))
]
