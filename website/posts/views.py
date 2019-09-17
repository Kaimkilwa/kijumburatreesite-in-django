from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import Post

# Create your views here.
class HomeView(ListView):

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'posts/index.html'
    context_object_name = "post_items"
    
class PostDetail(DetailView):
    model = Post
    template_name = 'posts/post_detail.html' 
 

