from django.contrib import admin
from .models import Contact,Produit,Article,Comment,TeamMember, Reply,Cart,CartItem
# Register your models here.


admin.site.register(Contact)
admin.site.register(Produit)
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(TeamMember)
admin.site.register(Reply)
admin.site.register(Cart)
admin.site.register(CartItem)
