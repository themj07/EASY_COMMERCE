from django.shortcuts import render , redirect
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from .models import Produit , Cart, CartItem
from django.db.models import Sum
from blog.models import *



# Create your views here.

def index_2(request):
    produits = Produit.objects.all()
    articles = Article.objects.all()
    members = TeamMember.objects.all()
    datas = {  
        'produits': produits,
        'articles' : articles,
        'members': members
    }
    return render(request, 'index_2.html', datas)


def index(request):
    produits = Produit.objects.all()
    articles = Article.objects.all()
    members = TeamMember.objects.all()
    datas = {
        'produits': produits,
        'articles' : articles,
        'members': members
    }
    return render(request, 'index.html', datas)


def navbar(request):
    datas = {
    }
    return render(request, 'navbar.html', datas)


def header(request):
    datas = {
    }
    return render(request, 'header.html', datas)


def cookie(request):
    datas = {
    }
    return render(request, 'cookie.html', datas)






def checkout(request):
    datas = {
    }
    return render(request, 'checkout.html', datas)


def shop(request):
    produits = Produit.objects.all()
    datas = {
        'produits': produits
    }
    return render(request, 'shop.html', datas)


def singleproduct(request, id):
    produits = Produit.objects.get(id=id)
    produitss = Produit.objects.all()
    comments = Comment.objects.all()
    datas = {
            'produits': produits,
            'comments': comments,
            'produitss' :produitss,
    }
    return render(request, 'singleproduct.html', datas)




def cart(request,id):  
    user = request.user
    p8 = Cart.objects.filter(user=user.id) 
    articles= Produit.objects.get(id=id) 
    product = get_object_or_404(Produit,id=id)
    cartItem , _ = CartItem.objects.get_or_create(user=user)
    order , created = Cart.objects.get_or_create(user=user , product=product)
    

    if created:
        cartItem.cart.add(order)
        q = order.quantity
        p = order.product.price
        
        pt =q*p
        order.prix_total=pt
        order.save()
        ptot= Cart.objects.aggregate(
        combined_age=Sum('prix_total')
        )
        cartItem.prix_total = ptot['combined_age'] 
        cartItem.save()
    else:
        x = order.quantity
        order.quantity = x
        order.save()
    
    datas = {
    'articles':articles,
    'p8':p8,
    }

    return redirect('page_cart')

def nombre(request,id, choice):
    user = request.user
    p8 = Cart.objects.filter(user=user) 
    articles= Produit.objects.get(id=id) 
    product = get_object_or_404(Produit,id=id)
    order= Cart.objects.get(user=user , product=product)
    cart = CartItem.objects.get(user=user)
    
    if choice == 'ajouter':
        order.quantity += 1
        q = order.quantity
        
        p = order.product.price
        
        pt =q*p
        order.prix_total=pt
        order.save()
        ptot= Cart.objects.aggregate(
        combined_age=Sum('prix_total')
        )
        cart.prix_total = ptot['combined_age'] 
        cart.save()
        
    elif choice == 'diminue':
        x= order.quantity
        if x  >= 2:
            order.quantity -= 1
            
        q = order.quantity
        p = order.product.price
        pt =q*p
        order.prix_total=pt
        order.save()
        ptot= Cart.objects.aggregate(
        combined_age=Sum('prix_total')
        )
        cart.prix_total = ptot['combined_age']

        cart.save()

    elif choice == 'supprimer':
        order.delete()
    

    
    datas = {
    'articles':articles,
    'p8':p8,
    }

    return redirect('page_cart')


def page_cart(request):
    user = request.user
    cart = CartItem.objects.get(user=user)
    p8 = Cart.objects.filter(user=user) 
    
    datas = {
    'p8':p8,
    'cart':cart,
    }
    return render(request,'cart.html',datas)