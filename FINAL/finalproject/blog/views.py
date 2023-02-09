from django.shortcuts import render
from django.shortcuts import render

from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_text
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.mail import send_mail, EmailMessage
from finalproject import settings
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.urls import reverse
from logging.config import valid_ident
from typing import Protocol
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from django.db.models.query_utils import Q
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .models import Article , TeamMember, Comment , Reply
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
