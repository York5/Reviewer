from django.contrib import admin
from webapp.models import Product, Review


class ReviewAdmin(admin.TabularInline):
    model = Review
    fields = ['author', 'product', 'text', 'rating']
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'category', 'description']
    list_filter = ['name', 'category']
    list_display_links = ['pk', 'name']
    search_fields = ['name', 'description']
    exclude = []
    inlines = [ReviewAdmin]
