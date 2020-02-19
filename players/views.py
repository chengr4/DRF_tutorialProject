# from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Player, Paradigm, Programmer
from .serializers import PlayerSerializer, ParadigmSerializer, ProgrammerSerializer


class PlayerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # get information from the database
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    # can be controlled in setting
    # permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)
    

class ParadigmViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # get information from the database
    queryset = Paradigm.objects.all()
    serializer_class = ParadigmSerializer

class ProgrammerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # get information from the database
    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer
