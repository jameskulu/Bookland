from django.contrib import admin
from .models import UsedCategory, UsedSubCategory, UsedProduct, UsedComment


admin.site.register(UsedCategory)
admin.site.register(UsedSubCategory)
admin.site.register(UsedProduct)
admin.site.register(UsedComment)
