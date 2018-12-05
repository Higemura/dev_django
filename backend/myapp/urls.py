from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'), # 127.0.0.1:8000/myapp
    path('index/', views.index, name='index'), # 127.0.0.1:8000/
]
