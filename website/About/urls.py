from django.urls import path
from .views import AboutComppany

urlpatterns = [
   
   
   path('about/', AboutComppany.as_view(), name='about')
  

]
