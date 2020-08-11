from .cart import Cart


def lengthCart(request):
    return {'cart': Cart(request)}
