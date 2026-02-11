from django.shortcuts import render, redirect
from blog.models import Post
from portfolio.models import Project
from catalog.models import Product
from leads.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.is_staff

def home(request):
    latest_posts = Post.objects.filter(status='PUBLISHED').order_by('-published_at')[:3]
    latest_projects = Project.objects.filter(is_active=True).order_by('-completed_date')[:3]
    # Featured products (limit to 2 for the homepage layout)
    featured_products = Product.objects.filter(is_active=True).order_by('-created_at')[:2]
    
    return render(request, 'core/home.html', {
        'latest_posts': latest_posts,
        'latest_projects': latest_projects,
        'featured_products': featured_products
    })

def about(request):
    return render(request, 'core/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            inquiry = form.save()
            
            # Email sending is temporarily disabled due to Render blocking SMTP ports.
            # Inquiries are saved to the database (Admin panel).
            # try:
            #     send_mail(
            #         subject,
            #         message,
            #         settings.DEFAULT_FROM_EMAIL,
            #         [settings.EMAIL_HOST_USER], # Send to admin (same as host user for now)
            #         fail_silently=False,
            #     )
            # except Exception as e:
            #     print(f"EMAIL ERROR: {e}")
            #     # Don't show error to user, just log it.
            
            messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
                
            return redirect('core:contact')
    else:
        form = ContactForm()
        
    return render(request, 'core/contact.html', {'form': form})

def testimonials(request):
    return render(request, 'core/testimonials.html')

@user_passes_test(is_admin)
def seo_dashboard(request):
    """
    A human-readable sitemap/SEO dashboard for admins.
    """
    links = [
        {'name': 'Homepage', 'url': reverse('core:home')},
        {'name': 'About Us', 'url': reverse('core:about')},
        {'name': 'Contact', 'url': reverse('core:contact')},
        {'name': 'Testimonials', 'url': reverse('core:testimonials')},
        {'name': 'Blog List', 'url': reverse('blog:post_list')},
        {'name': 'Services/Products', 'url': reverse('catalog:product_list')},
        {'name': 'Projects Portfolio', 'url': reverse('portfolio:project_list')},
    ]
    
    # Add some dynamic examples
    latest_post = Post.objects.filter(status='PUBLISHED').first()
    if latest_post:
        links.append({'name': f'Latest Post: {latest_post.title}', 'url': reverse('blog:post_detail', args=[latest_post.slug])})
        
    latest_prod = Product.objects.filter(is_active=True).first()
    if latest_prod:
        links.append({'name': f'Featured Product: {latest_prod.name}', 'url': reverse('catalog:product_detail', args=[latest_prod.slug])})

    return render(request, 'core/seo_dashboard.html', {'links': links})
