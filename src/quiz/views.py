from django.shortcuts import render
from rest_framework import generics
from .models import Category
from .serializer import CategorySerializer

# Create your views here.

class Category(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    
