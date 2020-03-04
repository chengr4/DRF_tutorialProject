# from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Patient
from .serializers import PatientSerializer

class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    # get information from the database
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    # can be controlled in setting
    # permissions_classes = (permissions.IsAuthenticatedOrReadOnly,)