from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index ,name="home"),
    path("login/home",views.index ,name="home"),
    path("login/userinfo",views.user_info,name="userinfo"),
    path("login/bill_prediction",views.register,name="register"),
    path("login/actual_bill",views.actual_bill,name="actual_bill"),
    path("login/suspect",views.suspect,name="suspect"),
    path("login",views.loginuser,name='login'),
    path('logout',views.logout_user,name='logout'),
    
]