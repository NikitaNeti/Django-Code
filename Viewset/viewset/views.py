from rest_framework.response import Response
from .models import *
from .serializers import ArticleSerializer
from rest_framework import status
from rest_framework import viewsets
 
class ArticleViewSet(viewsets.ViewSet):
   def list(self,request):
       arc = Article.objects.all()
       serializer = ArticleSerializer(arc, many=True)
       return Response(serializer.data)
 
   def create(self,request):
       serializer = ArticleSerializer(data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response(serializer.data, status=status.HTTP_201_CREATED)
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   def retrieve(self,request,pk=None):
       id=pk
       if id is not None:
           arc = Article.objects.get(id=id)
           serializer = ArticleSerializer(arc, many=True)
           return Response(serializer.data)
 
   def update(self,request,pk):
       id=pk
       arc = Article.objects.get(id=id)
       serializer = ArticleSerializer(arc,data=request.data)
       if serializer.is_valid():
           serializer.save()
           return Response({'msg':'Complete Data Updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   def partail_update(self,request,pk):
       id=pk
       arc = Article.objects.get(id=id)
       serializer = ArticleSerializer(arc,data=request.data,partial=True)
       if serializer.is_valid():
           serializer.save()
           return Response({'msg':'Partial Data Updated'})
       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
   def destroy(self,request,pk):
       id=pk
       arc = Article.objects.get(pk=id)
       arc.delete()
       return Response({'msg':'Data Deleted'})

