from django.db import models

# Create your models here.
class Like(models.Model):
    id = models.IntegerField(primary_key = True)
    sess_response = models.CharField(max_length=100)

class BT_Contact(models.Model):
    Contact_id = models.IntegerField(primary_key = True)
    First_Name =  models.CharField(max_length = 50,default='Default_name')
    Last_Name = models.CharField(max_length = 50,default= 'Default_lastname')
    Emailid = models.CharField(max_length= 100 ,default='Default@email.com')
    Message = models.CharField(max_length= 800 ,default= 'No_Message')

