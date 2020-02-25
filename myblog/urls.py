

from django.urls import path
from .views import blogview, detail

app_name = 'myblog'

urlpatterns = [

    path('', blogview, name = 'blogview'),
    path('<int:blog_id>/', detail, name='detail'),
] 
 