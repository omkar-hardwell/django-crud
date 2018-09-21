from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department
from .models import Employee
from .forms import DepartmentForm


# Create your views here.
def index(request):
    """Index view.
    :param request: Obj - Request.
    :return: str - HttpResponse response.
    """
    return HttpResponse("Hello, world. You're at the index.")


def departments(request):
    """Show departments detail.
    :param request: Obj - Request.
    :return: Render to department view.
    """
    department_list = Department.objects.all()
    return render(
        request, 'departments.html', {'departments': department_list})


def add_department(request):
    """Add department.
    :param request: Obj - Request.
    :return: Renders to departments view on saved or add department page.
    """
    if request.method == 'POST':
        form = DepartmentForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/departments')
            except:
                pass
    else:
        form = DepartmentForm()
    return render(
        request, 'department_add.html', {'form': form})


def edit_department(request, department_id):
    """Edit department.
    :param request: Obj - Request.
    :param department_id: int - Unique identification of department.
    :return: Render to edit department page.
    """
    department = Department.objects.get(department_id=department_id)
    return render(
        request, 'department_edit.html', {'department': department})


def update_department(request, department_id):
    """Update department.
    :param request: Obj - Request.
    :param department_id: int - Unique identification of department.
    :return: Renders to departments view on update or edit department page.
    """
    department = Department.objects.get(department_id=department_id)
    form = DepartmentForm(request.POST, instance=department)
    if form.is_valid():
        form.save()
        return redirect('/departments')
    return render(
        request, 'department_edit.html', {'department': department})


def delete_department(request, department_id):
    """Delete department.
    :param request: Obj - Request.
    :param department_id: int - Unique identification of department.
    :return: Renders to departments view on delete.
    """
    department = Department.objects.get(department_id=department_id)
    department.delete()
    return redirect('/departments')


def employees(request):
    """Show employees detail.
    :param request: Obj - Request.
    :return: Render to employee view.
    """
    employee_list = Employee.objects.all()
    return render(
        request, 'employees.html', {'employees': employee_list})
