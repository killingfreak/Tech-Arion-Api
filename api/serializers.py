from csv import field_size_limit
from dataclasses import fields
from pyexpat import model
from api.models import site1
from rest_framework import serializers

class site1_serializer(serializers.ModelSerializer):
    pro_name=serializers.CharField(max_length=50)
    pro_image=serializers.ImageField()
    pro_quantity=serializers.IntegerField()
    pro_size=serializers.CharField(max_length=20)
    pro_discription=serializers.CharField(max_length=50)
    pro_star=serializers.IntegerField()
    class Meta:
        model = site1
        fields = ['pro_name','pro_image','pro_quantity','pro_size','pro_discription','pro_star']