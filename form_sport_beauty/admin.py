from django.contrib import admin

# Register your models here.

from .models import RegistrationSportBeauty, Category, Item

admin.site.register(RegistrationSportBeauty)
admin.site.register(Category)
admin.site.register(Item)