from django.shortcuts import redirect, render
from .models import Article, Comment , Reply , Contact
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404

def index(request):
    articles = Article.objects.all()
    datas = {
        'articles' : articles,
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

def news(request):
    articles = Article.objects.filter(is_approved=True)
    datas = {
        'articles' : articles
    }
    return render(request, 'news.html', datas)

def singlenews(request, id):
    articles = Article.objects.get(id = id)
    comments = Comment.objects.all()
    replys = Reply.objects.all()
    datas = {
        'articles' : articles,
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


def create_news(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        create_news = Article()
        create_news.title = title
        create_news.author = author 
        create_news.description = description
        create_news.image = image
        create_news.save()

        return redirect('news')

    return render(request, 'create_annonce.html')



@login_required
@permission_required('blog.change_article', raise_exception=True)
def admin_articles(request):
    articles = Article.objects.all()
    return render(request, 'admin_articles.html', {'articles': articles})

@login_required
@permission_required('blog.change_article', raise_exception=True)
def approve_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.is_approved = True
    article.save()
    return redirect('admin_articles')

@login_required
@permission_required('blog.delete_article', raise_exception=True)
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect('admin_articles')