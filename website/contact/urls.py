from django.urls import path
from .views import Contactviiew ,AddMesage

urlpatterns = [
   
   path('contact/', Contactviiew.as_view(), name='contactview'),
    path('AddedMesage/', AddMesage , name='AddMesage'),
 
  

]
