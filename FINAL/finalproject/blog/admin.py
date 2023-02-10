from django.contrib import admin
from .models import Article,Comment,TeamMember, Reply , Contact

# Register your models here.

admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(TeamMember)
admin.site.register(Reply)
admin.site.register(Contact)
