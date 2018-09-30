from django.shortcuts import render, redirect, render_to_response
from django.contrib.auth import authenticate, login, logout
from .models import Department, Employee, GenderChoice
from .forms import DepartmentForm, EmployeeForm


# Create your views here.
def index(request):
    """Index view.
    :param request: Obj - Request.
    :return: str - HttpResponse response.
    """
    if is_authenticated(request):
        return redirect('/home')
    return render(request, 'login.html')


def departments(request):
    """Show departments detail.
    :param request: Obj - Request.
    :return: Render to department view.
    """
    if not is_authenticated(request):
        return redirect('/login')
    department_list = Department.objects.all()
    return render(
        request, 'departments.html', {'departments': department_list})


def add_department(request):
    """Add department.
    :param request: Obj - Request.
    :return: Renders to departments view on saved or add department page.
    """
    if not is_authenticated(request):
        return redirect('/login')
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
    if not is_authenticated(request):
        return redirect('/login')
    department = Department.objects.get(department_id=department_id)
    return render(
        request, 'department_edit.html', {'department': department})


def update_department(request, department_id):
    """Update department.
    :param request: Obj - Request.
    :param department_id: int - Unique identification of department.
    :return: Renders to departments view on update or edit department page.
    """
    if not is_authenticated(request):
        return redirect('/login')
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
    if not is_authenticated(request):
        return redirect('/login')
    department = Department.objects.get(department_id=department_id)
    department.delete()
    return redirect('/departments')


def employees(request):
    """Show employees detail.
    :param request: Obj - Request.
    :return: Render to employee view.
    """
    if not is_authenticated(request):
        return redirect('/login')
    employee_list = Employee.objects.all()
    return render(
        request, 'employees.html', {'employees': employee_list})


def add_employee(request):
    """Add employee.
    :param request: Obj - Request.
    :return: Renders to employees view on saved or add employee page.
    """
    if not is_authenticated(request):
        return redirect('/login')
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
    if not is_authenticated(request):
        return redirect('/login')
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
    if not is_authenticated(request):
        return redirect('/login')
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
    if not is_authenticated(request):
        return redirect('/login')
    employee = Employee.objects.get(employee_id=employee_id)
    employee.delete()
    return redirect('/employees')


def authenticate_user(request):
    """Authenticate user.
    :param request: Obj - Request.
    :return: Renders to home page otherwise login page.
    """
    if is_authenticated(request):
        return redirect('/home')
    username = password = ''
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # login(request, user)
            request.session['member_id'] = username
            return redirect('/home')
    return render(request, 'login.html')


def log_out(request):
    """Logged out and terminate the session of user.
    :param request: Obj - Request.
    :return: Renders to logout page.
    """
    # logout(request)
    try:
        del request.session['member_id']
    except KeyError:
        pass
    return render_to_response('logout.html')


def home_page(request):
    """Redirects to home page.
    :param request: Obj - Request.
    :return: Renders to the home page.
    """
    if not is_authenticated(request):
        return redirect('/login')
    return render(request, 'home.html')


def is_authenticated(request):
    """Check user session in exists.
    :param request: Obj - Request.
    :return: bool - True if session exists else False.
    """
    try:
        request.session['member_id']
    except KeyError:
        return False
    return True
