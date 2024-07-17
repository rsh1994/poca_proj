# marketplace/admin.py
from django.contrib import admin
from .models import PhotoCard, Sale, User

admin.site.register(PhotoCard)
admin.site.register(Sale)
admin.site.register(User)
