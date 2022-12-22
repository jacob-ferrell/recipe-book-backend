from django.db import models
import string
import random

def generate_unique_code():
    length = 6

    while True:
        code = ''.join(random.choices(string.ascii_uppercase, k=length))
        if Recipe.objects.filter(code=code).count() == 0:
            break

    return code

# Create your models here.
class Ingredient(models.Model):

    amount = models.TextField()

    name = models.TextField()


class Recipe(models.Model):

    name = models.TextField()

    description = models.TextField()


    created_at = models.DateTimeField(auto_now_add=True)