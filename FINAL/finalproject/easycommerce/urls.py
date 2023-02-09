"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from  . import views
from .views import index_2



urlpatterns = [   
    path('', index_2, name='index_2'),
    path('about', views.about, name='about'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('contact', views.contact, name='contact'),
    path('index', views.index, name='index'),
    path('news', views.news, name='news'),
    path('shop', views.shop, name='shop'),
    path('reply', views.reply, name='reply'),
    path('singlenews/<int:id>', views.singlenews, name='singlenews'),
    path('singleproduct/<int:id>', views.singleproduct, name='singleproduct'),
    path('login', views.custom_login, name='login'),
    path('navbar', views.navbar, name='navbar'),
    path('register', views.register, name='register'),
    path('logout', views.custom_logout, name='logout'),
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
    path('profile/<username>', views.profile, name='profile'),
    path("password_change", views.password_change, name="password_change"),
    path("password_reset", views.password_reset_request, name="password_reset"),
    path('reset/<uidb64>/<token>', views.passwordResetConfirm, name='password_reset_confirm'),
]