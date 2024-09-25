from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Movie, Category, Comment
from .serializers import MovieSerializer, CategorySerializer, CommentSerializer

# Create your views here.



class MovieAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                movie = Movie.objects.get(pk=pk)
                serializer = MovieSerializer(movie)
                return Response(serializer.data)
            except:
                return Response({"message": "Topilmadi!"})
        else:
            movies = Movie.objects.all()
            serializer = MovieSerializer(movies, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if not pk:
            serializer = MovieSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def put(self, request, pk=None):
        if pk:
            movie = Movie.objects.get(pk=pk)
            serializer = MovieSerializer(movie, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def delete(self, request, pk=None):
        if pk:
            movie = Movie.objects.get(pk=pk)
            movie.delete()
            return Response({"message": "O'chirildi!"})
        return Response({"message": "Xatolik!"})



class CategoryAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                category = Category.objects.get(pk=pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data)
            except:
                return Response({"message": "Topilmadi!"})
        else:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if not pk:
            serializer = CategorySerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def put(self, request, pk=None):
        if pk:
            category = Category.objects.get(pk=pk)
            serializer = CategorySerializer(category, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def delete(self, request, pk=None):
        if pk:
            category = Category.objects.get(pk=pk)
            category.delete()
            return Response({"message": "O'chirildi!"})
        return Response({"message": "Xatolik!"})


class CommentAPIView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                comment = Comment.objects.get(pk=pk)
                serializer = CommentSerializer(comment)
                return Response(serializer.data)
            except:
                return Response({"message": "Topilmadi!"})
        else:
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many=True)
            return Response(serializer.data)
    
    def post(self, request, pk=None):
        if not pk:
            serializer = CommentSerializer(data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def put(self, request, pk=None):
        if pk:
            comment = Comment.objects.get(pk=pk)
            serializer = CommentSerializer(comment, data=request.data)
            serializer.is_valid()
            serializer.save()
            return Response(serializer.data)
        return Response({"message": "Xatolik!"})
    
    def delete(self, request, pk=None):
        if pk:
            comment = Comment.objects.get(pk=pk)
            comment.delete()
            return Response({"message": "O'chirildi!"})
        return Response({"message": "Xatolik!"})


