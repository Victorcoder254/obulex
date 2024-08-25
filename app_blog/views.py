from django.shortcuts import render, get_object_or_404# Ensure this template existsfrom django.shortcuts import render, get_object_or_404
from .models import *
from app_home.models import *  # Import About model

def blog_view(request):
    posts = BlogPost.objects.all().order_by('-created')
    footer_info = FooterContactInfo.objects.last()  # Fetch the first instance of FooterInfo
    
    context = {
        'posts': posts,
        'footer_info': footer_info,
    }
    return render(request, 'files/home_blog.html', context)

def blog_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    footer_info = FooterContactInfo.objects.last()  # Fetch the first instance of FooterInfo

    context = {
        'post': post,
        'footer_info': footer_info,
    }
    return render(request, 'files/detail.html', context)

