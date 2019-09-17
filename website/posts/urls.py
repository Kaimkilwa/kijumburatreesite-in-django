

from django.urls import path
from .views import HomeView,PostDetail

urlpatterns = [
   
   path('', HomeView.as_view(), name='home'),
   path('post/<slug:slug>/', PostDetail.as_view(), name='post_detail'),

]
 