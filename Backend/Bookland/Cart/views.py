from django.shortcuts import render, redirect
from Books.models import Product
from django.contrib import messages
from .cart import Cart


def cart_detail(request):
    carts = Cart(request)
    cart = carts.list()
    context = {
        'cart': carts,
    }
    print(cart)
    return render(request, 'Cart/cart_detail.html', context)


def add_to_cart(request, id):
    if request.method == 'POST':
        product = Product.objects.get(id=id)
        quantity = int(request.POST['quantity'])

        if not quantity:
            quantity = 1
        cart = Cart(request)
        cart.add(product, quantity)
        messages.success(request, 'Book added to cart')
        return redirect('cart-detail')


def update_cart(request, id):
    if request.method == 'POST':
        data = request.POST
        quantity = data['quantity']
        cart = Cart(request)
        cart.update_cart(quantity, id)

        context = {
            'cart': cart
        }
        messages.success(request, 'Cart Updated')
    else:
        return redirect('cart-detail')

    return render(request, 'Cart/cart_detail.html', context)


def remove_from_cart(request, id):
    cart = Cart(request)
    cart.delete_cart(id)
    context = {
        'cart': cart
    }
    messages.success(request, 'Book removed from cart')
    return render(request, 'Cart/cart_detail.html', context)
