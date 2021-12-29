from django.urls import path
from .views import ListEmployee, DetailEmployee

urlpatterns = [
    path('<int:pk>/', DetailEmployee.as_view()),
    path('', ListEmployee.as_view()),
]