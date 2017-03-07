from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddProductForm
from .models import LookBookPage, Category, Product, SoonProduct
# Create your views here.


def home_page(request):

    return render(request, 'shop/base.html')


def look_book_page(request):
    look_items = LookBookPage.objects.all()
    return render(request, 'shop/lukaku.html', context={'look_items': look_items})


def soon_page(request):
    soon_items = SoonProduct.objects.all()
    context = {
        'soon_items': soon_items,
    }

    return render(request, 'shop/soon.html', context)


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    context = {
        'category': category,
        'categories': categories,
        'products': products,
    }

    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product,
                                                        })
