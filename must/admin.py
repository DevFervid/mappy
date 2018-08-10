from django.contrib import admin

# Register your models here.
from .models import Item, Category

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name','description','location','image','created_at','updated_at']
    list_filter = ['created_at', 'updated_at']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Item, ItemAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)
