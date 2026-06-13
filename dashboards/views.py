from django.db import DatabaseError
from django.utils.text import slugify
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import BlogPostForm, CategoryForm
import logging

logger = logging.getLogger(__name__)


# Create your views here.
@login_required(login_url='login')
def dashboard(request):

    category_count = Category.objects.all().count()
    posts_count = Blog.objects.all().count()

    context = {
        'category_count' : category_count,
        'posts_count' : posts_count
    }


    return render(request, 'dashboards/dashboard.html', context)

# category Crund Functions

def categories(request):

    return render(request, 'dashboards/categories.html')

def add_category(request):
    
    if request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category_form.save()
            return redirect('categories')
    else:
        category_form = CategoryForm()

    context = {
        'category_form' : category_form,
    }
    return render(request, 'dashboards/add_category.html', context)

def edit_category(request, pk):

    category = get_object_or_404(Category, pk=pk)

    if request.method == 'POST':
        category_EditForm = CategoryForm(request.POST, instance=category)
        if category_EditForm.is_valid():
            category_EditForm.save()
            return redirect('categories')
    else: 
        category_EditForm = CategoryForm(instance=category)

    context = {
        'category_EditForm' : category_EditForm,
        'category' : category
    }
    return render(request, 'dashboards/edit_category.html', context)

def delete_category(request, pk):

    category = get_object_or_404(Category, pk=pk)
    category.delete()
    return redirect('categories')

# Blog Post Related Function

def posts(request):

    posts = Blog.objects.all()
    context = {
        'posts' : posts
    }

    return render(request, 'dashboards/posts.html', context)
    
def add_post(request):

    if request.method == 'POST':
        blog_post_form = BlogPostForm(request.POST, request.FILES)
        if blog_post_form.is_valid():
            post = blog_post_form.save(commit=False) # Temporarly save form and get object form data in variable
            post.author = request.user  #add Author then save 
            post.save()
            
            # Save slug
            title = blog_post_form.cleaned_data['title']
            post.slug = slugify(title) + '-' + str(post.id)
            # post.slug = f"{slugify(post.title)}-{post.id}"
            post.save()
            
            return redirect('posts')
        # else:
        #     print('Form is In-Valid')
        #     print(blog_post_form.errors)

    else:
        blog_post_form = BlogPostForm()
    
    context = {
        'blog_post_form' : blog_post_form
    }

    return render(request, 'dashboards/add_post.html', context)


def edit_post(request, pk):
    post = get_object_or_404(Blog, pk=pk)
    
    if request.method == 'POST':
        blog_post_EditForm = BlogPostForm(request.POST, request.FILES, instance=post)
        if blog_post_EditForm.is_valid():
            updatedPost = blog_post_EditForm.save()
            title = blog_post_EditForm.cleaned_data['title']
            updatedPost.slug = slugify(title) + '-' + str(updatedPost.id)
            updatedPost.save()
            return redirect('posts')
    else:
        blog_post_EditForm = BlogPostForm(instance=post)

    context = {
        'blog_post_EditForm' : blog_post_EditForm,
        'post' : post
    }

    return render(request, 'dashboards/edit_post.html', context)

def delete_post(request, pk):
    
    post = get_object_or_404(Blog, pk=pk)

    post.delete()
    return redirect('posts')