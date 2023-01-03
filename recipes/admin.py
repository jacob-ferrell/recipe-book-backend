from django.contrib import admin
from .models import Recipe, Ingredient

# Register your models here.
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'quantity', 'unit', 'name')

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)