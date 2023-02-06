from django.shortcuts import render
from .models import Contact

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
from .forms import UserRegistrationForm , SetPasswordForm, PasswordResetForm, UserLoginForm
from .tokens import account_activation_token
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import UserUpdateForm
from .models import Produit , Article , TeamMember, Comment , Cart, Order , Reply



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



def about(request):
    members = TeamMember.objects.all()
    datas = {
        'members': members
    }
    return render(request, 'about.html', datas)



def checkout(request):
    datas = {
    }
    return render(request, 'checkout.html', datas)


def header(request):
    datas = {
    }
    return render(request, 'header.html', datas)


def cookie(request):
    datas = {
    }
    return render(request, 'cookie.html', datas)


def contact(request):
    datas = {
    }
    return render(request, 'contact.html', datas)


def news(request):
    articles = Article.objects.all()
    datas = {
        'articles' : articles
    }
    return render(request, 'news.html', datas)



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



def cart(request, id):
    produits = Produit.objects.get(id=id)
    produitss = Produit.objects.all()
    datas = {
        'produitss' :produitss,
        'produits': produits,
        
    }
    return render(request, 'cart.html', datas)


def add_to_cart(request, id):
    user = request.user
    produits = get_object_or_404(Produit, id=id)
    cart , _ = Cart.objects.get_or_create(user = user)
    order , created = Order.objects.get_or_create(user = user , ordered = False , product = produits)
    if created :
        cart.orders.add(order)
        cart.save()
    else :
        order.quantity += 1   
        order.save()
    
    return redirect(reverse('singleproduct' , kwargs= {'id' : id}))


def navbar(request):
    datas = {
    }
    return render(request, 'navbar.html', datas)


# def login(request):
#     datas = {
#     }
#     return render(request, 'login.html', datas)


def register(request):
    datas = {
    }
    return render(request, 'register.html', datas)

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


from django.shortcuts import render, redirect
from .models import Comment 


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
        nom = request.POST.get('nom')
        message = request.POST.get('message')
        
        reply = Reply() 
        reply.nom = nom
        reply.message = message
        reply.comment = Comment.objects.get(id=request.POST.get('comment_id'))
        reply.save()
    return render(request, 'singlenews.html')




def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, "Thank you for your email confirmation. Now you can login your account.")
        return redirect('login')
    else:
        messages.error(request, "Activation link is invalid!")

    return redirect('index_2')


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect('login')

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="register.html",
        context={"form": form}
        )
    
def activateEmail(request, user, to_email):
    mail_subject = "Activate your user account."
    message = render_to_string("template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        "protocol": 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear <b>{user}</b>, please go to you email <b>{to_email}</b> inbox and click on \
                received activation link to confirm and complete the registration. <b>Note:</b> Check your spam folder.')
    else:
        messages.error(request, f'Problem sending email to {to_email}, check if you typed it correctly.')



@login_required
def custom_logout(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("index_2")


def profile(request, username):
    if request.method == 'POST':
        user = request.user
        form = UserUpdateForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            user_form = form.save()

            messages.success(request, f'Your profile has been updated successfully!')
            return redirect('profile', user_form.username)

        for error in list(form.errors.values()):
            messages.error(request, error)

    user = get_user_model().objects.filter(username=username).first()
    if user:
        form = UserUpdateForm(instance=user)
        return render(request, 'profile.html', context={'form': form})

    return redirect("index_2")


def password_change(request):
    user = request.user
    if request.method == 'POST':
        form = SetPasswordForm(user, request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your password has been changed")
            return redirect('login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    form = SetPasswordForm(user)
    return render(request, 'password_reset_confirm.html', {'form': form})


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('homepage')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )

def passwordResetConfirm(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Your password has been set. You may go ahead and <b>log in </b> now.")
                return redirect('index_2')
            else:
                for error in list(form.errors.values()):
                    messages.error(request, error)

        form = SetPasswordForm(user)
        return render(request, 'password_reset_confirm.html', {'form': form})
    else:
        messages.error(request, "Link is expired")

    messages.error(request, 'Something went wrong, redirecting back to Homepage')
    return redirect("index_2")


def password_reset_request(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            user_email = form.cleaned_data['email']
            associated_user = get_user_model().objects.filter(Q(email=user_email)).first()
            if associated_user:
                subject = "Password Reset request"
                message = render_to_string("template_reset_password.html", {
                    'user': associated_user,
                    'domain': get_current_site(request).domain,
                    'uid': urlsafe_base64_encode(force_bytes(associated_user.pk)),
                    'token': account_activation_token.make_token(associated_user),
                    "protocol": 'https' if request.is_secure() else 'http'
                })
                email = EmailMessage(subject, message, to=[associated_user.email])
                if email.send():
                    messages.success(request,
                        """
                        <h2>Password reset sent</h2><hr>
                        <p>
                            We've emailed you instructions for setting your password, if an account exists with the email you entered. 
                            You should receive them shortly.<br>If you don't receive an email, please make sure you've entered the address 
                            you registered with, and check your spam folder.
                        </p>
                        """
                    )
                else:
                    messages.error(request, "Problem sending reset password email, <b>SERVER PROBLEM</b>")

            return redirect('index_2')

        for key, error in list(form.errors.items()):
            if key == 'captcha' and error[0] == 'This field is required.':
                messages.error(request, "You must pass the reCAPTCHA test")
                continue

    form = PasswordResetForm()
    return render(
        request=request, 
        template_name="password_reset.html", 
        context={"form": form}
        )
    


    

def custom_login(request):
    if request.method == "POST":
        form = UserLoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data["username"],
                password=form.cleaned_data["password"],
            )
            if user is not None:
                login(request, user) 
                messages.success(request, f"Hello <b>{user.username}</b>! You have been logged in")
                return redirect("index_2")

        else:
            for key, error in list(form.errors.items()):
                if key == 'captcha' and error[0] == 'This field is required.':
                    messages.error(request, "You must pass the reCAPTCHA test")
                    continue
                
                messages.error(request, error) 

    form = UserLoginForm()

    return render(
        request=request,
        template_name="login.html",
        context={"form": form}
        )


