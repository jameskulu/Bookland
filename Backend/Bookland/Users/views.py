from django.shortcuts import render, redirect
from .forms import UserForm, UserProfileForm
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from Books.models import Product
from Checkout.models import CustomerOrder


@login_required
def profile(request):
    return render(request, 'Users/manage_profile.html')


@login_required
def edit_profile(request):
    edit_profile_msg = ''
    message = ''
    if request.method == 'POST':
        user_form = UserForm(request.POST,
                             instance=request.user)
        profile_form = UserProfileForm(
            request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was updated successfully')
            return redirect('manage-profile')
        else:
            edit_profile_msg = 'Username is already taken'
            # return redirect('edit-profile')

        if edit_profile_msg:
            message = edit_profile_msg

    else:
        user_form = UserForm(instance=request.user)
        profile_form = UserProfileForm(instance=request.user.profile)

    print(edit_profile_msg)
    context = {
        'message': message,
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'Users/edit_profile.html', context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(
                request, 'Your password was successfully updated!')
            return redirect('manage-profile')

    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'Users/change_password.html', context)


@login_required()
def favrioute_list(request):
    products = Product.objects.filter(favrioute__id=request.user.id)

    context = {
        'products': products,
    }

    return render(request, 'Users/wishlist.html', context)


@login_required()
def my_orders(request):
    orders = CustomerOrder.objects.filter(customer=request.user)
    context = {
        'orders': orders,
    }
    return render(request, 'Users/orders.html', context)


@login_required
def cancel_book(request, pk):
    books = CustomerOrder.objects.get(pk=pk)
    user = request.user
    if books.customer != user:
        return HttpResponse('You are not authorized to view this page.')
    if request.method == 'POST':
        books.delete()
        messages.error(
            request, f"Your order was cancelled successfully.")
        return redirect('orders')
    context = {
        'books': books,
    }
    return render(request, 'Users/cancel_book.html', context)
