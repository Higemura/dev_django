from django import forms # フォームをinport
from .models import Day

# 日付をformで作成する
class DayCreateForm(forms.ModelForm): # 引数にforms.Formというのもある
  class Meta:
    model = Day #対象となるmodel
    fields = '__all__' # modelのfields（フィールド）。特定のものを指定する場合 ('title', 'text', 'date')のようにタプル型にする