from django.views import generic
from .forms import SearchForm
from .models import Employee

class IndexView(generic.ListView):
  # template_name = 'employee/employee_list.html'
  model = Employee
  paginate_by = 1

  def get_context_data(self):
    context = super().get_context_data()
    context['form'] = SearchForm(self.request.GET) #基の辞書にformを追加
    return context

  def get_queryset(self):
    form = SearchForm(self.request.GET)
    form.is_valid() #これをしないと、cleaned_dataができない

    #まずは全社員を取得
    queryset = super().get_queryset()

    #部署の選択があれば部署で絞込み
    department = form.cleaned_data['department']
    if department:
      queryset = queryset.filter(department=department)

    
    #サークルの選択があればサークルで絞込み
    club = form.cleaned_data['club']
    if club:
      queryset = queryset.filter(club=club)
    return queryset