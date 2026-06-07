from django.http import HttpResponse
from django.shortcuts import redirect, render,get_object_or_404

from blogs.models import Blog, Category


# Create your views here.


def post_by_category(request, category_id):

    # implemented in Context Processor
    # categories = Category.objects.all() 
    # print(categories.query)

    # one Way to handle error if not getting 
    category_name = get_object_or_404(Category, id=category_id)
    
    # Second way to handle if category not found
    # try:
    #     # category_name = categories.filter(id=category_id).first()
    #     category_name = Category.objects.get(id=category_id)
    # except:
    #     # redirect the user to homepage
    #     return redirect('home')
    
    posts = Blog.objects.filter(status='Published', category =category_id)
    # print(posts.query)

    context = {
        # 'categories'        : categories,
        'posts'             : posts,
        'category_name'     : category_name
    }
    return render(request, 'post_by_category.html', context)
    
    
