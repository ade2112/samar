from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def product_list(request):
    products = Product.objects.filter(is_active=True)
    categories = Category.objects.all()
    
    # Filter by category if provided
    category_slug = request.GET.get('category')
    if category_slug:
        products = products.filter(category__slug=category_slug)
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query) | products.filter(short_description__icontains=query)
    
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'catalog/product_list.html', context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)
