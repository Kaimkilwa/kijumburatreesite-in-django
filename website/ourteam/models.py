
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class MembersModel(models.Model):
	title= models. CharField(max_length =200 ,unique= True)
	name= models.CharField( null=True, blank=True,max_length =200 ,unique= True)
	slug = models.SlugField( null = True,max_length=200, unique=True)
	Description = models.TextField( null=True, blank= True)
	pic = models.FileField(upload_to='images/', null=True, blank=True)
	created_on = models.DateTimeField(auto_now_add=True)
	updated_on = models.DateTimeField(auto_now= True)
	status = models.IntegerField(choices=STATUS, default=0)

	class Meta:
		ordering = ['-created_on']
		verbose_name_plural ="Members"
	def __str__(self):
		return self.title
