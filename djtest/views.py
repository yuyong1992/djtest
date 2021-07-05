from django.shortcuts import render
from rest_framework import viewsets
from djtest import models
from djtest import serializer


# Create your views here.
class ModuleView(viewsets.ModelViewSet):
    queryset = models.Module.objects.all()
    serializer_class = serializer.ModuleSerializer


class ApiView(viewsets.ModelViewSet):
    queryset = models.Api.objects.all()
    serializer_class = serializer.ApiSerializer
