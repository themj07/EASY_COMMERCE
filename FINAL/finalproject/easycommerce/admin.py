from django.contrib import admin
from .models import Produit,Cart,CartItem
# Register your models here.

admin.site.register(Produit)
admin.site.register(Cart)
admin.site.register(CartItem)
