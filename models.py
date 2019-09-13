from django.db import models

# Create your models here.
class Like(models.Model):
    id = models.IntegerField(primary_key = True)
    sess_response = models.CharField(max_length=100)

