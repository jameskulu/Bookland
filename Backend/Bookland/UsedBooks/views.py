from django.core.files.storage import FileSystemStorage
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CommentForm, UsedProductForm
from .models import UsedCategory, UsedSubCategory, UsedProduct, UsedComment
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def used_books(request):
    products = UsedProduct.objects.order_by('-published_date')[:15]
    categories = UsedCategory.objects.all()[0:3]
    context = {
        'products': products,
        'usedcategories': categories,
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

    paginator = Paginator(categories, 9)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)

    if is_valid_queryparam(name):
        categories = categories.filter(title__icontains=name)
        paginator = Paginator(categories, 9)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

    if is_valid_queryparam(subcategory):
        categories = categories.filter(subcategory__name=subcategory)
        paginator = Paginator(categories, 9)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

    if is_valid_queryparam(minvalue):
        categories = categories.filter(price__gte=minvalue)
        paginator = Paginator(categories, 9)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

    if is_valid_queryparam(maxvalue):
        categories = categories.filter(price__lt=maxvalue)
        paginator = Paginator(categories, 9)
        page = request.GET.get('page')
        try:
            post_list = paginator.page(page)
        except PageNotAnInteger:
            post_list = paginator.page(1)
        except EmptyPage:
            post_list = paginator.page(paginator.num_pages)

    context = {
        'usedcategories': categories,
        'slug': slug,
        'usedsubcategories': subcategories,
        'maincategorys': maincategorys,
        'page_obj': post_list,
        'name': name,
        'minvalue': minvalue,
        'maxvalue': maxvalue,
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


@login_required
def listed_books(request):
    used_products = UsedProduct.objects.filter(
        user=request.user).order_by('-published_date')
    context = {
        'used_products': used_products,
    }
    return render(request, 'UsedBooks/listed_books.html', context)


@login_required
def category_form(request):
    categories = UsedCategory.objects.all()
    if request.method == 'POST':
        value = request.POST['cats']
        request.session['value'] = value
        return redirect('book-post')
        # print(value)
    return render(request, 'UsedBooks/category_form.html', {'categories': categories, })


# @login_required
# def book_post(request):

#     subcategories = UsedSubCategory.objects.filter(
#         category__name=request.session['value'])
#     print(subcategories)

#     form = UsedProductForm()
#     if request.method == 'POST':
#         form = UsedProductForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             obj.save()
#             return redirect('listed-books')
#     context = {
#         'form': form,
#         'subcategories': subcategories,
#     }
#     return render(request, 'UsedBooks/uploadbook.html', context)


@login_required
def book_post(request):
    subcategories = UsedSubCategory.objects.filter(
        category__name=request.session['value'])
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        description = request.POST['description']
        price = request.POST['price']
        image = request.FILES.get('image')
        subcategory = request.POST['subcategory']

        hello = UsedSubCategory.objects.get(id=subcategory)

        UsedProduct.objects.create(
            title=title,
            author=author,
            description=description,
            price=price,
            subcategory=hello,
            user=request.user,
            image=image
        )
        messages.success(request, 'Your book was uploaded successfully.')
        return redirect('listed-books')

    return render(request, 'UsedBooks/uploadbook.html', {'subcategories': subcategories})


class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = UsedProduct
    fields = ['title', 'description', 'author',
              'image', 'price']
    template_name = 'UsedBooks/edit_uploadbook.html'
    success_url = '/used-books/listed-books'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form_valid = super().form_valid(form)
        messages.success(self.request, "Updated successfully")
        return form_valid

    def test_func(self):
        book = self.get_object()
        if self.request.user == book.user:
            return True
        return False


@login_required
def delete_book(request, pk):
    books = UsedProduct.objects.get(pk=pk)
    user = request.user
    if books.user != user:
        return HttpResponse('You are not authorized to view this page.')
    if request.method == 'POST':
        books.delete()
        messages.error(request, "Your book was deleted successfully.")
        return redirect('listed-books')
    context = {
        'books': books,
    }
    return render(request, 'UsedBooks/delete_book.html', context)
