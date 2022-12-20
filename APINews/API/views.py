from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.views import APIView
from django.http import Http404

from rest_framework import generics,mixins

from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions

from .customauth import CustomAuthentication

# Create your views here.

@csrf_exempt
def article_list(request):
   if request.method == 'GET':
       articles = Article.objects.all()
       serializer = ArticleSerializer(articles,many=True)
       return JsonResponse(serializer.data,safe=False)
 
   elif request.method == 'POST':
       data = JSONParser().parse(request)
       serializer = ArticleSerializer(data=data)
 
       if serializer.is_valid():
           serializer.save()
           return JsonResponse(serializer.data,status = 201)
       return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        snippet = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ArticleSerializer(snippet)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(snippet, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        snippet.delete()
        return HttpResponse(status=204)


''' API_Views decorator in function based API VIEWS '''

@api_view(['GET', 'POST'])
def article_list(request):

    if request.method == 'GET':
        snippets = Article.objects.all()
        serializer = ArticleSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
def article_detail(request,pk):
    try:
        snippet = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ArticleSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

'''CLASS BASED VIEWS '''

class ArticleList(APIView):
    def get(self,request,format=None):
        snippets = Article.objects.all()
        serializer = ArticleSerializer(snippets,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ArticleDetail(APIView):
    def get_object(self,pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet)
        return Response(serializer.data)

    def put(self,request,pk,format=None):
        snippet = self.get_object(pk)
        serializer = ArticleSerializer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)

    def delete(self,request,pk,format=None):
        snippet = self.get_object(pk)
        return Response(status=status.HTTP_204_NO_CONTENT)


'''Mixins and GenericAPIView'''

class GenericAPIView(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.RetrieveModelMixin,mixins.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field ='id'

    authenticatin_classes = [CustomAuthentication]
    permission_classes = [IsAuthenticated]

    # authenticatin_classes = [TokenAuthentication]
    # permission_classes = [DjangoModelPermissions]


    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)
    def post(self,request,id):
        return self.create(request,id)

class DetailGenericAPI(mixins.ListModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field ='id'

    authenticatin_classes = [CustomAuthentication]

    # permission_classes = [IsAdminUser]
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticatedOrReadOnly]
    # permission_classes = [DjangoModelPermissions]
                
    def get(self,request,id=None):
        if id:
            return self.retrieve(request)
        else:
            return self.list(request)               

    def put(self,request,id=None):
        return self.update(request,id)  

    def delete(self,request,id):
        return self.destroy(request,id)

''' Using generic class based views '''

class Genericlist(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    

class GenericDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    lookup_field ='id'


