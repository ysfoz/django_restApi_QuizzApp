from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .models import Category, Question, Quiz
from .serializer import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
from .pagination import MyPagination

# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
class CategoryDetail(generics.ListAPIView):   
    serializer_class = CategoryDetailSerializer
  
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category =self.kwargs['category']
        queryset = queryset.filter(category__name = category)
        return queryset
    

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = MyPagination
    
    def get_queryset(self):
        querySet = Question.objects.all()
        title = self.kwargs['title']
        querySet = querySet.filter(quiz__title = title)
        return querySet
        