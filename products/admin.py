from django.contrib import admin
from .models import Product, Category
from django.urls import reverse
from django.utils.html import format_html

# Register your models here.
admin.site.register(Category)




@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    def view_api_docs(self, obj):
        url = reverse('schema-swagger-ui')
        return format_html('<a href="{}" target="_blank">View API Docs</a>', url)

