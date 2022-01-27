from django.contrib import admin
from django.urls import path,include
from dictapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("dictapp.urls")),
]
