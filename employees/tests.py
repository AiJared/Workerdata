from django.test import TestCase
from .models import Employee

# Create your tests here.
class EmployeeModelTest(TestCase):
    @classmethod

    def setUpTestData(cls):
        Employee.objects.create(name='first employee', post='a post here')

    def test_name_content(self):
        employee = Employee.objects.get(id=1)
        expected_object_name = f'{employee.name}'
        self.assertEqual(expected_object_name, 'first employee')

    def test_post_content(self):
        employee = Employee.objects.get(id=1)
        expected_object_name = f'{employee.post}'
        self.assertEqual(expected_object_name, 'a post here')