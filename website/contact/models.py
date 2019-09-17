from django.db import models
from django.contrib.auth.models import User
# Create your models here.
STATUS = (
    (0,"Draft"),
    (1,"Publish")
)
class ContactModel(models.Model):
    email= models. CharField(max_length =200 ,unique= True)
    slug = models.SlugField( null = True,max_length=200, unique=True)
    message = models.TextField( null=True, blank= True)
    adress =models .TextField(null= True, blank= True)
    PHone_number= models.CharField(max_length= 100,unique = True, null=True, blank =True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    class Meta:
        ordering = ['-created_on']
        verbose_name_plural ="Customer Contact"

    def __str__(self):
        return self.email
