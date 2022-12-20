from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Ingredient(models.Model):

    amount = models.TextField()

    name = models.TextField()


class Recipe(models.Model):

    name = models.TextField()

    description = models.TextField()

    ingredients = models.ManyToManyField('recipes.Ingredient', related_name='recipes_with_ingredient')
