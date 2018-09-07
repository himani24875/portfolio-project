from django.shortcuts import render, get_object_or_404

from .models import Blog

def allBlogs(request):
    blogs = Blog.objects
    return render(request, 'blog/allBlogs.html', {'blogs':blogs})

def detailBlog(request, blog_id):
    blogDetail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detailBlog.html', {'blog':blogDetail})
