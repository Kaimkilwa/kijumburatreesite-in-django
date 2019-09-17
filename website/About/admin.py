from django.contrib import admin
from .models import AboutModel
# Register your models here.

class ViewAbout(admin.ModelAdmin):
	list_display = ( 'title','created_on')
	list_filter = ("title",'created_on')
	search_fields = ['title', 'created_on']
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(AboutModel,ViewAbout)
