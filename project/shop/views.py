from django.shortcuts import render, get_object_or_404, redirect
from cart.forms import CartAddProductForm
from .models import Category, Product


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()

    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})


def favourite_add(request, id):
    product = get_object_or_404(Product, id=id)
    if product.objects.filter(id=product.id).exists():
        product.objects.remove(product.id)
    else:
        product.objects.add(product.id)   
    return redirect('shop:favourite_list')         

def favourite_list(request):
    new = Product.objects.filter(favourites=request.user)
    return render(request,
                  'shop/favourites.html',
                  {'new': new})                   
