from django.shortcuts import get_object_or_404, render
from blogs.models import Category, Blog
from assignments.models import About, SocialLink

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