from django.shortcuts import render
from django.http import HttpResponse
from .models import Department


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
