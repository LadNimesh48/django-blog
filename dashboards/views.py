from django.db import DatabaseError
from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, Category

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CategoryForm
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


    
    
    

