from django.contrib import admin

# Register your models here.
from .models import Item

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','location','image','created_at','updated_at']

admin.site.register(Item, ItemAdmin)
