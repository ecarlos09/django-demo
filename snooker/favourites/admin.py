from django.contrib import admin

from .models import Nationality, Player

# Register your models here.

admin.site.register(Nationality)
admin.site.register(Player)