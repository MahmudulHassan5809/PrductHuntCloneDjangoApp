from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
	list_display = ('id' , 'title' , 'image' , 'pub_date')
	list_display_links = ('id' , 'title')

	search_fields = ('title',)
	list_per_page = 25


# Register your models here.
admin.site.register(Product , ProductAdmin)
