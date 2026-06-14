from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render,get_object_or_404

from blogs.models import Blog, Category, Comment
from django.db.models import Q


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
    

def blogs(request, slug):

    single_blog = get_object_or_404(Blog, slug=slug, status='Published')


    if request.method == 'POST':
        comment = Comment()
        comment.user = request.user
        comment.blog = single_blog
        comment.comment = request.POST['comment']
        comment.save()
        return HttpResponseRedirect(request.path_info)

    # Get Comments
    comments = Comment.objects.filter(blog = single_blog)
    comment_count = comments.count()


    context = {
        'single_blog'   :   single_blog,
        'comments' : comments,
        'comment_count' : comment_count
    }

    return render(request, 'blogs.html', context)



def search(request):
    keyword = request.GET.get('keyword')
    blogs = Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword), status='Published')
    # print(blogs)

    context = {
        'blogs'   :   blogs,
        'keyword'   : keyword
    }


    return render(request, 'search.html', context)