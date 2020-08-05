from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Cart.cart import Cart
from .models import CustomerLocation, CustomerOrder
from django.contrib import messages
from django.core.mail import send_mail


@login_required()
def checkout(request):
    carts = Cart(request)
    cart = carts.list()
    # print(cart)
    total_price = 0
    for i in range(0, len(cart)):
        total_price += cart[i]['price']

    if request.method == 'POST':
        company = request.POST['company']
        street_address = request.POST['street_address']
        city = request.POST['city']
        country = request.POST['country']

        c = CustomerLocation.objects.create(
            customer=request.user,
            company=company,
            street_address=street_address,
            city=city,
            country=country
        )
        for i in range(0, len(cart)):
            CustomerOrder.objects.create(
                customer=request.user,
                product=cart[i]['obj'],
                quantity=cart[i]['quantity'],
                price=cart[i]['price'],
                location=c,
                phone_number=request.user.profile.phone
            )

        send_mail(
            'Bookland',
            f'Hi {request.user.first_name} {request.user.last_name}, Your order has been placed successfully. We will contact you after few day for the delivery. Your total amount is Rs.{total_price}.00 .Keep Shopping :)',
            'jameskulu55@gmail.com',
            [f'{request.user.email}'],
            fail_silently=True,
        )
        messages.success(
            request, 'Your order has been placed successfuly. Please check your email for the confirmation.')
        return redirect('home')

    context = {
        'cart': carts,
    }
    return render(request, 'Checkout/checkout.html', context)
