from django.contrib.auth.models import User, Group
from rest_framework import serializers
from recipe_api.main_app.models import Recipe, RecipeGroup

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Recipe
        fields = ('name', 'details', 'owner')


class RecipeGroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RecipeGroup
        fields = ('name', 'recipes')