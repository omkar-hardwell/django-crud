from django import forms
from .models import Department, Employee


class DepartmentForm(forms.ModelForm):
    """Department form for Add and Edit operations."""
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeForm(forms.ModelForm):
    """Employee form for Add and Edit operations."""
    class Meta:
        model = Employee
        fields = "__all__"
