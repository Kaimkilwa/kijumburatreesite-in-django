from django.shortcuts import render
from .models import ContactModel
from django.views.generic import ListView,DetailView,CreateView
# Create your views here.
class Contactviiew(ListView):
	model=ContactModel
	template_name = "contact/contact.html"
	context_object_name = "contact_info"

def AddMesage(request):
	if request.method == "POST": #checking if the request method is a POST
		if "taskAdd" in request.POST: #checking if there is a request to add a todo
			email = request.POST["email"] #title
			message = request.POST["message"] #category
			infor = ContactModel( email= email,  message= message )
			infor.save() #saving the todo 
			return redirect("/") #reloading the page
