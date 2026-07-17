from django.shortcuts import render
from api.models import StudentModel
from api.serializers import StudentSerializer
from rest_framework import viewsets

# Create your views here.

class StudentModelViewset(viewsets.ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer