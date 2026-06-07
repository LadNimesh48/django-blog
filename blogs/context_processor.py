

from assignments.models import SocialLink
from blogs.models import Category

# category context processor
def get_categories(request):
    
    categories = Category.objects.all()
    return dict(categories=categories)

# Social links context processor
def get_social_links(request):
    
    socialLink = SocialLink.objects.all()
    return dict(socialLink=socialLink)