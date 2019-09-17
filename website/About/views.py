from django.shortcuts import render
from django.views.generic import ListView
from .models import AboutModel
# Create your views here.
class AboutComppany(ListView):
	model=AboutModel
	template_name = "about/about.html"
	context_object_name = "obj_about"