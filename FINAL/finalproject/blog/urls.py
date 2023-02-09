from django.urls import path
from . import views


urlpatterns = [ 
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('singlenews/<int:id>', views.singlenews, name='singlenews'), 
    path('reply', views.reply, name='reply'),
]