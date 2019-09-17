from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import MembersModel

# Create your views here.
class MemberView(ListView):

    queryset = MembersModel.objects.filter(status=1).order_by('-created_on')
    template_name = 'members/members.html'
    context_object_name = "menbersobj"
# class PostDetail(DetailView):
#     model = Post
#     template_name = 'posts/post_detail.html' 
 

