from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Department, Employee, GenderChoice
from .forms import DepartmentForm, EmployeeForm


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


def add_employee(request):
    """Add employee.
    :param request: Obj - Request.
    :return: Renders to employees view on saved or add employee page.
    """
    department_list = Department.objects.all()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        print(form)
        if form.is_valid():
            try:
                form.save()
                return redirect('/employees')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(
        request, 'employee_add.html',
        {'form': form, 'departments': department_list})


def edit_employee(request, employee_id):
    """Edit employee.
    :param request: Obj - Request.
    :param employee_id: int - Unique identification of employee.
    :return: Render to edit employee page.
    """
    department_list = Department.objects.all()
    employee = Employee.objects.get(employee_id=employee_id)
    return render(
        request, 'employee_edit.html',
        {'employee': employee,
         'departments': department_list,
         'gender_choices':
             [GenderChoice.choices()[0][0], GenderChoice.choices()[1][0]]})


def update_employee(request, employee_id):
    """Update employee.
    :param request: Obj - Request.
    :param employee_id: int - Unique identification of employee.
    :return: Renders to employees view on update or edit employee page.
    """
    department_list = Department.objects.all()
    employee = Employee.objects.get(employee_id=employee_id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('/employees')
    return render(
        request, 'employee_edit.html',
        {'employee': employee,
         'departments': department_list,
         'gender_choices':
             [GenderChoice.choices()[0][0], GenderChoice.choices()[1][0]]})


def delete_employee(request, employee_id):
    """Delete employee.
    :param request: Obj - Request.
    :param employee_id: int - Unique identification of department.
    :return: Renders to employees view on delete.
    """
    employee = Employee.objects.get(employee_id=employee_id)
    employee.delete()
    return redirect('/employees')
