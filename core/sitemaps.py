from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post
from catalog.models import Product
from portfolio.models import Project

class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return ['core:home', 'core:about', 'core:contact', 'blog:post_list', 'catalog:product_list', 'portfolio:project_list']

    def location(self, item):
        return reverse(item)

class PostSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.8

    def items(self):
        return Post.objects.filter(status='PUBLISHED')

    def lastmod(self, obj):
        return obj.updated_at

class ProductSitemap(sitemaps.Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return Product.objects.filter(is_active=True)
        
    def lastmod(self, obj):
        # Assuming Product doesn't have updated_at, using created_at or None
        return obj.created_at

class ProjectSitemap(sitemaps.Sitemap):
    changefreq = 'monthly'
    priority = 0.7

    def items(self):
        return Project.objects.filter(is_active=True)

    def lastmod(self, obj):
        return obj.updated_at
