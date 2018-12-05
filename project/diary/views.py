from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import generic
from .forms import DayCreateForm
from .models import Day


# class型のview
class IndexView(generic.ListView): #generic.ListViewを継承したclassを作成
  model = Day
  # template_name = 'diary/my_list.html' これでも可だが別途 my_list.htmlを作成する必要がある


class AddView(generic.CreateView):
  model = Day
  form_class = DayCreateForm
  # fields = '__all__' #単縦な汎用viewならform.pyが不要な為はこれでもOK
  success_url = reverse_lazy('diary:index') #データ追加が成功した時のリダイレクト先


class UpdateView(generic.UpdateView):
  model = Day
  form_class = DayCreateForm
  success_url = reverse_lazy('diary:index')


class DeleteView(generic.DeleteView):
  model = Day
  success_url = reverse_lazy('diary:index')


class DetailView(generic.DetailView):
  model = Day
