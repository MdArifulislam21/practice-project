from django.shortcuts import render, get_object_or_404

from .models import Blog


def blogview(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/blog.html', {'blogs':blogs} )


def detail(request, blog_id):
	blog_obj = get_object_or_404(Blog, pk=blog_id)
	return render(request, 'blogs/detail.html', {'blog_obj':blog_obj} )



