from django.contrib import admin
from .models import *
# Register your models here.
class admin1(admin.ModelAdmin):
    list_display=('pro_name','pro_image','pro_quantity','pro_size','pro_discription','pro_star')


admin.site.register(site1)