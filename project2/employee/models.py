from django.db import models
from django.utils import timezone

# 部署
class Department(models.Model):
  name = models.CharField('部署名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)

  def __str__(self): # 特殊メソッド__str__を使うことで選択項目をわかりやすくする（self.name）
    return self.name

# 部活
class Club(models.Model):
  name = models.CharField('部活名', max_length=20)
  created_at = models.DateTimeField('日付', default=timezone.now)

  def __str__(self): # 特殊メソッド__str__を使うことで選択項目をわかりやすくする（self.name）
    return self.name


class Employee(models.Model):
  first_name = models.CharField('名', max_length=20)
  last_name = models.CharField('姓', max_length=20)
  email = models.EmailField('メールアドレス', blank=True) # EmailFieldはメール形式じゃないとエラーを出す。blank=Trueで空文字列だけどもOKにする
  department = models.ForeignKey(
    Department, verbose_name='部署', on_delete=models.PROTECT, # models.PROTECTで部署と紐付いた従業員がいる場合部署を削除できなくする。CASCADEで関連していても削除できる
  )
  club = models.ManyToManyField(
    Club, verbose_name='部活', # 第一引数にClubと紐付ける。verbose_nameは説明名
  )
  created_at = models.DateTimeField('日付', default=timezone.now) # 社員を作成した日付
  # address = models.CharField('住所', max_length=20, default="aaa") # defaultはblank=Trueで空白OKにもできる
  models.OneToOneField

  # コメント

  def __str__(self):
    return '{0} {1} {2}'.format(self.last_name, self.first_name, self.department)