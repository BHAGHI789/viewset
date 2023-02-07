from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from app.models import student
from app.serializer import Studentserializer

# Create your views here.
class Studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=student.objects.all()
        serializer=Studentserializer(queryset,many=True)
        return Response(serializer.data)
    def retrive(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=student.objects.get(pk=id)
            serializer=Studentserializer(queryset,data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response('complte the data')
    def destroy(self,request,pk):
        id=pk
        queryset=student.objects.get(pk=id)
        queryset.delete()
        return Response('item was deleted')
    def create(self,request):
        queryset=student.objects.all()
        serializer=Studentserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("the item was created")