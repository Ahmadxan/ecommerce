from django.shortcuts import render
from products.models import Category, Product


def home_page(request):
    categories = Category.objects.all()
    products = Product.objects.all()

    ctx = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'product/index.html', ctx)


def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    products = Product.objects.all()
    ctx = {
        'product': product,
        'products': products,
    }
    return render(request, 'product/product-detail.html', ctx)