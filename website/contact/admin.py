from django.contrib import admin
from .models import ContactModel
# Register your models here.
class ViewMeassage(admin.ModelAdmin):
	list_display = ( 'email', 'message','created_on')
	list_filter = ("message",'created_on')
	search_fields = ['message', 'created_on']
	
admin.site.register(ContactModel,ViewMeassage)