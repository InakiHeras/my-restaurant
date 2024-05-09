from django.contrib import admin
from .models import Dish
# Register your models here.
class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'precio')
    search_fields = ['name', 'description']

admin.site.register(Dish, DishAdmin)