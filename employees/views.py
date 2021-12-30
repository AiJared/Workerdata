from django.shortcuts import render
from rest_framework import generics
from .permissions import IsSuperUserOrReadOnly
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class ListEmployee(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class DetailEmployee(generics.RetrieveAPIView):
    permission_classes = (IsSuperUserOrReadOnly)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer