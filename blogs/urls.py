
from django.urls import path

from blogs import views


urlpatterns = [
    
    path('<int:category_id>', views.post_by_category, name='post_by_category'),

]