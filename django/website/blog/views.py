from django.shortcuts import render, get_object_or_404
from .models import Post

def allpost(request):
    posts = Post.objects
    return render(request, 'posts.html', {'posts': posts})

def detail(request, blog_id):
    post_detail = get_object_or_404(Post, pk = blog_id)
    return render(request, 'post_detail.html', {'post': post_detail})