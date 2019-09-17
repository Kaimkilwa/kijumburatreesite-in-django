from django.contrib import admin
from .models import MembersModel
# Register your models here.
class Members(admin.ModelAdmin):
    list_display = ('title', 'slug','name' ,'status','created_on','pic','updated_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(MembersModel,Members) 