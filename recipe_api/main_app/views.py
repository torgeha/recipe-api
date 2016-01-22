from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from recipe_api.main_app.serializers import UserSerializer, GroupSerializer, RecipeSerializer, RecipeGroupSerializer
from recipe_api.main_app.models import Recipe, RecipeGroup

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited
    """

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipes to be viewed or edited
    """

    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeGroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows recipeGroups to be viewed or edited
    """

    queryset = RecipeGroup.objects.all()
    serializer_class = RecipeGroupSerializer