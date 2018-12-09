from django.views import generic
from .models import Employee

class IndexView(generic.ListView):
  # template_name = 'employee/employee_list.html'
  model = Employee