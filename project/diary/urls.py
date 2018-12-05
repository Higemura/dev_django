from django.urls import path
from . import views

app_name = 'diary'

urlpatterns = [
    path('', views.index, name='index'), # /daiary
    path('add/', views.add, name='add'), # /diary/add
    path('update/<int:pk>/', views.update, name='update'), # /diary/update/1 <int:pk> はint（整数）のpk（primary_key）に紐付ける
    path('delete/<int:pk>/', views.delete, name='delete'), # /diary/delete/1
    path('detail/<int:pk>/', views.detail, name='detail'), # /diary/detail/1
]
