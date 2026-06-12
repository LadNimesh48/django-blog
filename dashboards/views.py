from django.shortcuts import render

from blogs.models import Blog, Category

from django.contrib.auth.decorators import login_required


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