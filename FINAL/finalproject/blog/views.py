from django.shortcuts import render
from .models import Article , TeamMember, Comment , Reply , Contact
from easycommerce.models import *


def about(request):
    members = TeamMember.objects.all()
    datas = {
        'members': members
    }
    return render(request, 'about.html', datas)


def news(request):
    articles = Article.objects.all()
    datas = {
        'articles' : articles
    }
    return render(request, 'news.html', datas)

def singlenews(request, id):
    articles = Article.objects.get(id = id)
    produits = Produit.objects.all()
    comments = Comment.objects.all()
    replys = Reply.objects.all()
    datas = {
        'articles' : articles,
        'produits': produits,
        'comments' : comments,
        'replys' : replys
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        comment = request.POST.get('comment')
        if name and email and comment:
            c = Comment(name=name, email=email, comment=comment)
            c.save()
            
    return render(request, 'singlenews.html', datas)


def reply(request) : 
    if request.method == 'POST' : 
        nom = request.POST.get('nom', '')
        message = request.POST.get('message', '')
        comment = Comment.objects.get(id=id)
        reply, created = Reply.objects.get_or_create(comment=comment)
        
        reply.nom = nom
        reply.message = message
        reply.save()
    return render(request, 'singlenews.html')


def contact(request) : 
    if request.method == 'POST' : 
        nom = request.POST.get('name')
        email = request.POST.get('email')
        com = request.POST.get('subject')
        
        
        contact = Contact()
        contact.nom = nom
        contact.email = email 
        contact.commentaire = com 
        contact.save()
        
    return render(request, 'contact.html')