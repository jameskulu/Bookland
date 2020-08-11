from django.conf import settings
from Books.models import Product
from decimal import Decimal


class Cart(object):
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_KEY)
        if not cart:
            cart = self.session[settings.CART_SESSION_KEY] = {}
        self.cart = cart
        # print(self.cart)

    def add(self, product, quantity):
        product_id = str(product.id)

        if not product_id in self.cart:
            self.cart[product_id] = {
                'quantity': quantity, 'price': str(product.price)}
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        self.session.modified = True

    def list(self):
        carts = []
        for product_id in self.cart.keys():
            obj = Product.objects.get(id=product_id)
            tmp_cart = {
                'id': product_id,
                'obj': obj,
                'quantity': self.cart[product_id]['quantity'],
                'price': Decimal(int(self.cart[product_id]['quantity']) * float(obj.price))
            }
            carts.append(tmp_cart)

        return carts

    def get_total_amount(self):
        return sum([Decimal(item['quantity'] * item['price']) for item in self.cart.values()])

    def update_cart(self, quantity, product_id):
        pid = str(product_id)
        self.cart[pid]['quantity'] = int(quantity)
        self.save()

    def delete_cart(self, product_id):
        pid = str(product_id)
        del self.cart[pid]
        self.save()

    def clear_cart(self):
        del self.session[settings.CART_SESSION_KEY]
        self.save()

    def __len__(self):
        return sum([int(item.get('quantity')) for item in self.cart.values()])
