from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('Accounts.urls')),
    path('', include('Books.urls')),
    path('users/', include('Users.urls')),
    path('', include('Contact.urls')),
    path('cart/', include('Cart.urls')),
    path('used-books/', include('UsedBooks.urls')),
    path('checkout/', include('Checkout.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

handler404 = 'Books.views.error_404_view'
