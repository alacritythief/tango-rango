from django.contrib import admin

# Importing models from Rango app
from rango.models import Category, Page

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url', 'views')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'views', 'likes')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
