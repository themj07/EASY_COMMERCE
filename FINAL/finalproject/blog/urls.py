from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path( '',index, name='index'),
    path('news', views.news, name='news'),
    path('singlenews/<int:id>', views.singlenews, name='singlenews'), 
    path('contact', views.contact, name='contact'),
    path('create_annonce', views.create_news, name='create_annonce'),
    path('admin_articles/', views.admin_articles, name='admin_articles'),
    path('admin_approve/<int:pk>/', views.approve_article, name='approve_article'),
    path('admin_delete/<int:pk>/', views.delete_article, name='delete_article'),
]