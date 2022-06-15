from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title','parent','active', 'created', 'modified']
    fields = ['title','description','parent','listing_order','active']
    search_fields = ['title']
    
    def formfield_for_foreignkey(self, db_field, request, **kwargs):  
        if db_field.name == "parent":
            kwargs["queryset"] = Category.objects.filter(parent=None)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)
        