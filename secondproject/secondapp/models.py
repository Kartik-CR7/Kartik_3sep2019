from django.db import models

# Create your models here.
class studentdetails(models.Model):
    id = models.IntegerField(primary_key = True)
    First_Name =  models.CharField(max_length = 20)
    Last_Name = models.CharField(max_length = 20,default= None)
    Emailid = models.CharField(max_length= 20 ,default='sharmakartik21791@gmail.com')
