from django.contrib import admin
from .models import category, seller, product, order


admin.site.register(category)
admin.site.register(seller)
admin.site.register(product)
admin.site.register(order)
