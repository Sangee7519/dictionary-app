from django.contrib import admin
from django.urls import path
from dictapp import views

urlpatterns = [
    path("Dictionary",views.Dictionary),
    path("login",views.login),
    path("signup",views.signup),
    path("insert",views.insert),
    path("logintask",views.logintask),
    path("home",views.h),
    path("Quotes",views.Quotes),
    path("page1",views.page1),
    path("page2",views.page2),
    path("admin",views.admin),
    path("adminlogin",views.adminlogin),
    path('view',views.view),
    ]
