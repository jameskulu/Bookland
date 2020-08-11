from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from Cart.cart import Cart
from .models import CustomerLocation, CustomerOrder
from django.contrib import messages
from django.core.mail import send_mail
from tabulate import tabulate


@login_required()
def checkout(request):
    carts = Cart(request)
    cart = carts.list()

    hello = []
    for c in cart:
        a = [c['obj'], c['quantity'], f"Rs. {c['price']}.00",
             f"Rs. {c['price']*c['quantity']}.00"]
        hello.append(a)
    print(hello)

    headers = ['Book', 'Quantity', 'Unit Price', 'Price']

    new_list = tabulate(hello, headers=headers, tablefmt='orgtbl')

    total_price = 0
    for i in range(0, len(cart)):
        total_price += cart[i]['price']

    if request.method == 'POST':
        company = request.POST['company']
        street_address = request.POST['street_address']
        city = request.POST['city']
        country = request.POST['country']

        c, created = CustomerLocation.objects.get_or_create(
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
            f'Hi {request.user.first_name} {request.user.last_name}, Your order has been placed successfully.\n\
We will contact you after few day for the delivery.\n\
\n\
Your ordered books:\n\
{new_list}\n\
\n\
Your total amount is Rs.{total_price}.00.\nKeep Shopping :)',
            'jameskulu55@gmail.com',
            [f'{request.user.email}'],
            fail_silently=True,
        )

        carts.clear_cart()
        messages.success(
            request, 'Your order has been placed successfuly. Please check your email for the confirmation.')
        return redirect('home')

    context = {
        'cart': carts,
        'total_price': total_price
    }
    return render(request, 'Checkout/checkout.html', context)
