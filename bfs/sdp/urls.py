from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',Home,name="home"),
    path('login/',Login,name="login"),
    path('Register',Register,name="Register"),
    path('navbar',Navbar,name="nb"),
    path('navbar1',Navbar1,name="nb1"),
    path('home1',Home1,name="h1"),
    path('deposit',deposit,name="dep"),
    path('contact',contact,name="con"),
    path('credit',credit,name="cre"),
    path('products',products,name="pro"),
    path('profile',profile,name="profile"),
    path('fedb',fedb,name="fdb"),
    path('res',resp,name="res"),
    path('forgot',forgot,name="forgot"),
    path('forgotsent',forgotsent,name="fs"),
    path('forgotpass',forgotpassword),
    path('newpass',newpassword),
    path('depositsuccess',depositsuccess,name="depsuc"),
]