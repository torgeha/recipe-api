from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    details = models.TextField()
    owner = models.ForeignKey(User)
    #last_edited = models.DateField(auto_now=True) include at some point?


class RecipeGroup(models.Model):
    name = models.CharField(max_length=100)
    recipes = models.ManyToManyField(Recipe)