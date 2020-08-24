from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects
    return render(request, 'blog.html',{'blogs':blogs})

def details(request,blog_id):
    blogdet = get_object_or_404(Blog,pk = blog_id)
    return render(request, 'detail.html',{'blog':blogdet})