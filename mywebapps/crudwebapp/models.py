"""Database models."""
from django.db import models
from .utils import ChoiceEnum


# Create your models here.
class Department(models.Model):
    """Department model."""
    department_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "(department_id=%s, name='%s')" % (
            self.department_id, self.name)


class GenderChoice(ChoiceEnum):
    """Enumeration for gender choice for employee model."""
    male = 'Male'
    female = 'Female'


class Employee(models.Model):
    """Employee model."""
    employee_id = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=255, null=False)
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        null=False
    )
    date_of_join = models.DateField()
    gender = models.CharField(
        max_length=6,
        choices=GenderChoice.choices(),
        default=GenderChoice.male,
        null=False
    )
    address = models.CharField(max_length=1000, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    def __str__(self):
        return "(employee_id=%s, name='%s', department_id=%s, " \
            "date_of_joining='%s', gender='%s', address='%s', " \
            "salary=%s)" % (self.employee_id, self.name, self.department,
                            self.date_of_join, self.gender, self.address,
                            self.salary)
