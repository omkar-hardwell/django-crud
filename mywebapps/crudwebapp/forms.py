from django import forms
from .models import Department


class DepartmentForm(forms.ModelForm):
    """Department form for Add and Edit operations."""
    class Meta:
        model = Department
        fields = "__all__"
