from django.shortcuts import render, get_object_or_404
from .models import Category, SubCategory, Product


def index(request):
    products = Product.objects.order_by('-published_date')[:10]
    categories = Category.objects.all()[0:9]
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'Books/index.html', context)


def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    # products = Product.objects.get(pk=pk)
    # is_favrioute = False
    # if products.favrioute.filter(id=request.user.id).exists():
    #     is_favrioute = True
    context = {
        'products': products,
        # 'is_favrioute': is_favrioute,
    }
    return render(request, 'Books/product_detail.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def categoryView(request, slug):
    categories = Product.objects.filter(subcategory__category__name=slug)
    subcategories = SubCategory.objects.filter(category__name=slug)

    name = request.GET.get('name')
    minvalue = request.GET.get('minvalue')
    maxvalue = request.GET.get('maxvalue')
    subcategory = request.GET.get('subcategory')

    if is_valid_queryparam(name):
        categories = categories.filter(title__icontains=name)

    if is_valid_queryparam(subcategory):
        categories = categories.filter(subcategory__name=subcategory)

    if is_valid_queryparam(minvalue):
        categories = categories.filter(price__gte=minvalue)

    if is_valid_queryparam(maxvalue):
        categories = categories.filter(price__lt=maxvalue)

    return render(request, 'Product/category.html', {'categories': categories, 'slug': slug, 'subcategories': subcategories, })
