from django.shortcuts import render
from blog.models import Post

def home(request):
    latest_posts = Post.objects.filter(status='PUBLISHED').order_by('-published_at')[:3]
    return render(request, 'core/home.html', {'latest_posts': latest_posts})

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    return render(request, 'core/contact.html')

def testimonials(request):
    return render(request, 'core/testimonials.html')
