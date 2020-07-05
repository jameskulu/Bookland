from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, SubCategory, Product, Comment
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from Contact.forms import SubscribeForm


def index(request):
    products = Product.objects.order_by('-published_date')[:10]
    categories = Category.objects.all()[0:9]
    form = SubscribeForm()
    context = {
        'products': products,
        'categories': categories,
        'form': form,
    }
    return render(request, 'Books/index.html', context)


def product_detail(request, pk):
    products = get_object_or_404(Product, pk=pk)
    comments = Comment.objects.filter(product=products).order_by('-time_stamp')
    # products = Product.objects.get(pk=pk)

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(
                product=products, user=request.user, content=content)
            comment.save()
            return redirect('product-detail', products.id)
    else:
        form = CommentForm()

    is_favrioute = False
    if products.favrioute.filter(id=request.user.id).exists():
        is_favrioute = True
    context = {
        'products': products,
        'is_favrioute': is_favrioute,
        'comments': comments,
        'form': form,
    }
    return render(request, 'Books/product_detail.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def categoryView(request, slug):
    maincategorys = Category.objects.all()
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

    context = {
        'categories': categories,
        'slug': slug,
        'subcategories': subcategories,
        'maincategorys': maincategorys
    }

    return render(request, 'Books/category.html', context)


@login_required()
def wishlist(request, pk):
    products = get_object_or_404(Product, pk=pk)
    user = request.user

    if products.favrioute.filter(id=user.id).exists():
        products.favrioute.remove(user)
        messages.success(request, 'Removed from wishlist')
    else:
        products.favrioute.add(user)
        messages.success(request, 'Added to wishlist')
    return redirect('product-detail', pk=products.id)


def search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if is_valid_queryparam(q):
        queries = Product.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q) | Q(author__icontains=q))
        template_name = 'Books/main_search.html'
        context = {
            'queries': queries,
            'q': q,
        }
    else:
        return redirect('home')
    return render(request, template_name, context)


def error_404_view(request, exception):
    return render(request, 'Books/404.html')
