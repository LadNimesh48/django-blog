from django.shortcuts import get_object_or_404, redirect, render
from blogs.models import Category, Blog
from assignments.models import About, SocialLink

from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def home(request):

    # implemented in Context Processor
    # categories = Category.objects.all()
    # print(categories);

    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('created_at')
    # print(featured_posts);

    posts = Blog.objects.filter(is_featured=False, status='Published')

    # About from DB
    try:
        about = About.objects.get()
    except:
        about = None

    context = {
        # 'categories'        : categories,
        'featured_posts'    : featured_posts,
        'posts'             : posts,
        'about'             : about,
    }
    return render(request, 'home.html', context)


def register(request):

    if request.method == 'POST':
        # print(request.method)
        # print(request)
        registrationForm = RegistrationForm(request.POST)
        if registrationForm.is_valid():
            registrationForm.save()
            return redirect('login')
    else:
        registrationForm = RegistrationForm()

    context = {
        'registrationForm'  : registrationForm,
    }

    return render(request, 'register.html', context)

def login(request):

    if request.method == 'POST':

        loginForm = AuthenticationForm(request, request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']

            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)

            return redirect('dashboard')
    else:

        loginForm = AuthenticationForm()

    context = {
        'loginForm'  : loginForm,
    }

    return render(request, 'login.html', context)

def logout(request):
    
    auth.logout(request)

    return redirect('login')

