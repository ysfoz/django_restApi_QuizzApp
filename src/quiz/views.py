from django.db.models import query
from django.shortcuts import render
from rest_framework import generics
from .models import Category, Question, Quiz
from .serializer import CategorySerializer, CategoryDetailSerializer, QuestionSerializer
# from .pagination import MyPagination
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class CategoryList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticated]
    
class CategoryDetail(generics.ListAPIView):   
    serializer_class = CategoryDetailSerializer
    permission_classes = [IsAuthenticated]
  
    def get_queryset(self):
        queryset = Quiz.objects.all()
        category =self.kwargs['category']
        queryset = queryset.filter(category__name = category)
        return queryset
    

class QuizDetail(generics.ListAPIView):
    serializer_class = QuestionSerializer
    # pagination_class = MyPagination
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        querySet = Question.objects.all()
        title = self.kwargs['title']
        querySet = querySet.filter(quiz__title = title)
        return querySet
        