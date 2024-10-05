from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Employee
from .serializer import EmployeeSerializer

# Create your views here.
class EmployeeViewSet(ModelViewSet):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()