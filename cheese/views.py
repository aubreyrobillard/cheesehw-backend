from django.shortcuts import render
from .models import Cheese
from rest_framework import permissions
from rest_framework import viewsets
from .serializer import CheeseSerializer

class CheeseViewSet(viewsets.ModelViewSet):
    # the main query for the index route
    queryset = Cheese.objects.all()
    # serializer class for serializing output
    serializer_class = CheeseSerializer
    # optional permisson class set permission level
    permission_classes = [permissions.AllowAny]
