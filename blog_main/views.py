from django.shortcuts import render
from blogs.models import Category, Blog

def home(request):

    # implemented in Context Processor
    # categories = Category.objects.all()
    # print(categories);

    featured_posts = Blog.objects.filter(is_featured=True, status='Published').order_by('created_at')
    # print(featured_posts);

    posts = Blog.objects.filter(is_featured=False, status='Published')

    context = {
        # 'categories'        : categories,
        'featured_posts'    : featured_posts,
        'posts'             : posts
    }
    return render(request, 'home.html', context)