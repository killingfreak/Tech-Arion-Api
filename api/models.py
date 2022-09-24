from asyncio.windows_events import NULL
from distutils.command.upload import upload
from django.db import models



# Create your models here.
class site1(models.Model):
    pro_name=models.CharField(max_length=50)
    pro_image=models.ImageField(null=True)
    pro_quantity=models.IntegerField()
    pro_size=models.CharField(max_length=20)
    pro_discription=models.CharField(max_length=50)
    pro_star=models.IntegerField()
