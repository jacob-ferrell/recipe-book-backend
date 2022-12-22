from django.shortcuts import render
from rest_framework import generics
from .serializers import RecipeSerializer
from .models import Recipe

# Create your views here.

class RecipeView(generics.ListAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer