from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm
from .models import UsedCategory, UsedSubCategory, UsedProduct, UsedComment
from django.shortcuts import render, get_object_or_404, redirect


def used_books(request):
    products = UsedProduct.objects.order_by('-published_date')[:15]
    categories = UsedCategory.objects.all()[0:3]
    context = {
        'products': products,
        'categories': categories,
    }
    return render(request, 'UsedBooks/used_books.html', context)


def used_books_detail(request, pk):
    products = get_object_or_404(UsedProduct, pk=pk)
    comments = UsedComment.objects.filter(
        product=products).order_by('-time_stamp')

    if request.method == 'POST':

        form = CommentForm(request.POST)
        if form.is_valid():
            content = request.POST.get('content')
            comment = UsedComment.objects.create(
                product=products, user=request.user, content=content)
            comment.save()
            return redirect('used-books-detail', products.id)
    else:
        form = CommentForm()
    context = {
        'products': products,
        'comments': comments,
        'form': form,
    }
    return render(request, 'UsedBooks/used_books_detail.html', context)


def is_valid_queryparam(param):
    return param != '' and param is not None


def used_categoryView(request, slug):
    maincategorys = UsedCategory.objects.all()
    categories = UsedProduct.objects.filter(subcategory__category__name=slug)
    subcategories = UsedSubCategory.objects.filter(category__name=slug)

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

    return render(request, 'UsedBooks/used_books_category.html', context)


def used_search(request):
    try:
        q = request.GET.get('q')
    except:
        q = None
    if is_valid_queryparam(q):
        queries = UsedProduct.objects.filter(
            Q(title__icontains=q) | Q(description__icontains=q) | Q(author__icontains=q))
        template_name = 'UsedBooks/used_books_search.html'
        context = {
            'queries': queries,
            'q': q,
        }
    else:
        return redirect('used-books')
    return render(request, template_name, context)


def listed_books(request):
    used_products = UsedProduct.objects.filter(user=request.user)
    context = {
        'used_products': used_products,
    }
    return render(request, 'UsedBooks/listed_books.html', context)
