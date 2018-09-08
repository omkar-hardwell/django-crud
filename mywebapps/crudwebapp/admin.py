from django.contrib import admin
from .models import Department
from .models import Employee


# Register your models here.
admin.site.register(Department)
admin.site.register(Employee)
