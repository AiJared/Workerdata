from django.shortcuts import render
from rest_framework import generics
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class ListEmployee(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DetailEmployee(generics.RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer