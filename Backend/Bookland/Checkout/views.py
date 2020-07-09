from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Cart.cart import Cart
from .models import Order, OrderBook


@login_required()
def checkout(request):
    carts = Cart(request)
    cart = carts.list()

    if request.method == 'POST':
        company = request.POST['company']
        street_address = request.POST['street_address']
        city = request.POST['city']
        country = request.POST['country']

    context = {
        'cart': carts,
    }
    print('hello', cart)
    return render(request, 'Checkout/checkout.html', context)
