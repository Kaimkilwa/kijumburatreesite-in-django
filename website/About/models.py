

from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class AboutModel(models.Model):
	title= models. CharField(max_length =200 ,unique= True)
	subtitle= models. CharField( null=True, blank=True,max_length =200 ,unique= True)
	slug = models.SlugField( null = True,max_length=200, unique=True)
	content = models.TextField( null=True, blank= True)
	vision =models .TextField(null= True, blank= True)
	mission =models .TextField(null= True, blank= True)
	objective_aim =models .TextField(null= True, blank= True)
	organisation_structure  =models .TextField(null= True, blank= True)
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_on']
		verbose_name_plural ="About Company"
	def __str__(self):
		return self.title
