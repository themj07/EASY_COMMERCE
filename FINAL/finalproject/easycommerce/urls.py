from django.urls import path
from  . import views 
from .views import index_2



urlpatterns = [   
    path('', index_2, name='index_2'),
    path('cart',views.page_cart, name='page_cart'),
    path('cart/<int:id>', views.cart, name='cart'),
    path('cart/<int:id>/cart/<str:choice>',views.nombre, name='nombre'),
    path('checkout', views.checkout, name='checkout'),
    path('index', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('singleproduct/<int:id>', views.singleproduct, name='singleproduct'),
]