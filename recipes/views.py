from django.shortcuts import render
from rest_framework import viewsets
from .serializers import RecipeSerializer, IngredientSerializer
from .models import Recipe, Ingredient
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json


# Create your views here.

class RecipeView(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class IngredientView(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer

@csrf_exempt
def create_recipe(request):
    print(request.user, request.session.session_key)
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'})
    if not request.user.is_authenticated:
        return JsonResponse({'error': 'You must be logged in to perform this action'})
    data = json.loads(request.body)
    username = request.user.username
    name = data.get('name')
    description = data.get('description')
    recipe = Recipe.objects.create(name=name, description=description, username=username)
    recipe.save()
    return JsonResponse({'success': True})
