"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:z
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
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from graphene_django.views import GraphQLView
from easycommerce.schema import schema
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from easycommerce.models import *


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['url', 'nom', 'email', 'commentaire']

# ViewSets define the view behavior.
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    

class ProduitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produit
        fields = ['url', 'name', 'price', 'image' , 'description' , 'categorie']

# ViewSets define the view behavior.
class ProduitViewSet(viewsets.ModelViewSet):
    queryset = Produit.objects.all()
    serializer_class = ProduitSerializer
    



class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ['url', 'title', 'author', 'description' , 'image' ]

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    
    
    

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['url', 'name', 'email', 'comment']

# ViewSets define the view behavior.
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
  
  

class ReplySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Reply
        fields = ['url', 'nom', 'message', 'comment']

# ViewSets define the view behavior.
class ReplyViewSet(viewsets.ModelViewSet):
    queryset = Reply.objects.all()
    serializer_class = ReplySerializer
      
    

class TeamMemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['url', 'name', 'profession', 'facebook_link' , 'instagram_link' , 'photo' , 'description' ]

# ViewSets define the view behavior.
class TeamMemberViewSet(viewsets.ModelViewSet):
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    


class  OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['url', 'user', 'product', 'quantity' , 'ordered']

# ViewSets define the view behavior.
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
       

class  CartSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cart
        fields = ['url', 'user', 'orders', 'ordered' ]

# ViewSets define the view behavior.
class CartViewSet(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
         
    
    
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'Contact', ContactViewSet)
router.register(r'Produit', ProduitViewSet)
router.register(r'Article', ArticleViewSet)
router.register(r'Comment', CommentViewSet)
router.register(r'Reply', ReplyViewSet)
router.register(r'TeamMember', TeamMemberViewSet)
router.register(r'Order', OrderViewSet)
router.register(r'Cart', CartViewSet)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("easycommerce.urls")),
    path("graphql", GraphQLView.as_view(graphiql=True, schema=schema)),
    path('api-auth/', include('rest_framework.urls')),
    path('apirest', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
