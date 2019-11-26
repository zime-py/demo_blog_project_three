from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from my_first_blog import helpers

from .forms import ContactForm
from .models import *


def post_list(request):
    posts = Post.objects.all()
    posts = helpers.pg_records(request, posts, 2)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, id):  
    #-----------NEW----------------
    try:  
        post = Post.objects.get(id=id)
        context = {'post': post}
    #----------------NEW------------------    
    except:
        msg = "There is not post"  
        context = {'msg':msg}      
    return render(request, 'blog/post_detail.html', context)


def post_by_category(request, name):
    posts = Post.objects.filter(category__name = name)
    return render(request, 'blog/post_by_category.html', {'posts': posts})


def contact(request):
    if request.method == 'POST':
        f = ContactForm(request.POST)
        if f.is_valid():
            name = f.cleaned_data['name']
            sender = f.cleaned_data['email']
            subject = "You have a new Feedback from {}:{}".format(name, sender)
            message = "Subject: {}\n\nMessage: {}".format(f.cleaned_data['subject'], f.cleaned_data['message'])
            send_mail(subject, message, sender, ['mahmudhossain836@gmail.com'])
            f.save()
            messages.add_message(request, messages.INFO, 'Submitted.')
            return redirect('contact')
    else:
        f = ContactForm()
    return render(request, 'blog/contact.html', {'form': f})


def login(request):
    if request.user.is_authenticated:
        return redirect('admin_page')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            # correct username and password login the user
            auth.login(request, user)
            return redirect('admin_page')
        else:
            messages.error(request, 'Error wrong username/password')
 
    return render(request, 'blog/login.html')
 
def logout(request):
    auth.logout(request)
    return render(request,'blog/logout.html')
 
def admin_page(request):
    if not request.user.is_authenticated:
        return redirect('blog_login')       
 
    return render(request, 'cadmin/admin_page.html')

def me(request):
    #auth.logout(request)
    return render(request,'blog/me.html')
