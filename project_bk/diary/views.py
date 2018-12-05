from django.shortcuts import render, redirect, get_object_or_404
from .forms import DayCreateForm
from .models import Day

def index(request):
  context = {
    'day_list': Day.objects.all(), #データベースに保存されているデータを全て取得する
  }
  return render(request, 'diary/day_list.html', context)


def add(request):
  # 送信内容を基にフォームを作る。POSTじゃなければ空のフォーム
  form = DayCreateForm(request.POST or None)

  # method=POST の時の処理かつformの入力内容が問題なければ
  if request.method == 'POST' and form.is_valid():
    form.save() # modelがデータベースに保存される
    return redirect('diary:index') #リダイレクト先を指定

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
  context = {
    'form': form
  }
  return render(request, 'diary/day_form.html', context)

def update(request, pk):
  # urlのpkを基にDayを取得
  day = get_object_or_404(Day, pk=pk)

  form = DayCreateForm(request.POST or None, instance=day) #instance=day は取得したdayモデルに紐付ける

  # method=POST の時の処理かつformの入力内容が問題なければ
  if request.method == 'POST' and form.is_valid():
    form.save() # modelがデータベースに保存される
    return redirect('diary:index') #リダイレクト先を指定

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
  context = {
    'form': form
  }
  return render(request, 'diary/day_form.html', context)


def delete(request, pk):
  # urlのpkを基にDayを取得
  day = get_object_or_404(Day, pk=pk)

  # method=POST の時の処理かつformの入力内容が問題なければ
  if request.method == 'POST':
    day.delete() # dayインスタンスを削除する
    return redirect('diary:index') #リダイレクト先を指定

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
  context = {
    'day': day #dayモデルインスタンスを渡す
  }
  return render(request, 'diary/day_confirm_delete.html', context)


def detail(request, pk):
  # urlのpkを基にDayを取得
  day = get_object_or_404(Day, pk=pk)

  # 通常時のページアクセスや、入力内容に誤りがあればまたページを表示
  context = {
    'day': day #dayモデルインスタンスを渡す
  }
  return render(request, 'diary/day_detail.html', context)
