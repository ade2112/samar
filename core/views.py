from django.shortcuts import render, redirect
from blog.models import Post
from portfolio.models import Project
from catalog.models import Product
from leads.forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

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
            
            # Send email notification
            try:
                subject = f"New Inquiry from {inquiry.name}: {inquiry.subject}"
                message = f"""
                You have received a new inquiry from the website.
                
                Name: {inquiry.name}
                Email: {inquiry.email}
                Phone: {inquiry.phone}
                Subject: {inquiry.subject}
                
                Message:
                {inquiry.message}
                """
                send_mail(
                    subject,
                    message,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.EMAIL_HOST_USER], # Send to admin (same as host user for now)
                    fail_silently=False,
                )
                messages.success(request, 'Your message has been sent successfully! We will contact you soon.')
            except Exception as e:
                print(f"EMAIL ERROR: {e}")
                messages.warning(request, f'Your message was saved, but we could not send the email notification. Error: {e}')
                
            return redirect('core:contact')
    else:
        form = ContactForm()
        
    return render(request, 'core/contact.html', {'form': form})

def testimonials(request):
    return render(request, 'core/testimonials.html')
