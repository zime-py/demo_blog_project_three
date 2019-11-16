from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from blog.forms import PostForm
 
 
def post_add(request):
    
    if request.method == "POST":
      
        f = PostForm(request.POST)
        if f.is_valid():
            #  save data
            f.save()
            return redirect('post_add')
 
    # if request is GET the show unbound form to the user
    else:
        f = PostForm()
    return render(request, 'cadmin/post_add.html', {'form': f})

def account_info(request):
    return render(request, 'cadmin/account_info.html')


#------------New--------------------
#@login_required(login_url='blog_login')
def account_info(request):
    return render(request, 'cadmin/account_info.html')

#@login_required(login_url='blog_login')
def change_password(request):
    if request.method == "POST":
        u = request.user
        new_password = request.POST.get('new_password')
        u.set_password(new_password)
        u.save()
        s = 'success'
        return render(request, 'cadmin/password_change.html', {'s':s})
    return render(request, 'cadmin/password_change.html')

#------------New--------------------

def register(request):
    if request.method == 'POST':
        f = CustomUserCreationForm(request.POST)
        if f.is_valid():
            f.save()
            messages.success(request, 'Account created successfully')
            return redirect('register')
 
    else:
        f = CustomUserCreationForm()
 
    return render(request, 'blog/register.html', {'form': f})