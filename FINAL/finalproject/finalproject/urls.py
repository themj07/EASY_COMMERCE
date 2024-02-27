from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include
from user.models import *
from blog.models import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("blog.urls")),
    path('',include("user.urls")),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
