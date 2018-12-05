from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), # /daiary
    path('add/', views.AddView.as_view(), name='add'), # /diary/add
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'), # /diary/update/1 <int:pk> はint（整数）のpk（primary_key）に紐付ける
    path('delete/<int:pk>/', views.DeleteView.as_view(), name='delete'), # /diary/delete/1
    path('detail/<int:pk>/', views.DetailView.as_view(), name='detail'), # /diary/detail/1
]
