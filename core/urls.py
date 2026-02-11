from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('seo-dashboard/', views.seo_dashboard, name='seo_dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
