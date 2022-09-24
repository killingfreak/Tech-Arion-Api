from urllib import request
from django.shortcuts import render
from .models import *
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *

# Create your views here.

@api_view(['GET'])
def api1(request):
    item=site1.objects.all()
    serializer = site1_serializer(item,many=True)
    return Response({'status':"sucess","data":serializer.data})

@api_view(['get'])
def api2(request,id):
    item=site1.objects.get(id=id)
    serializer = site1_serializer(item)
    return Response({"status":"sucess","data":serializer.data})
    