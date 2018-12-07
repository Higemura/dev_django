from django.db import models
from django.utils import timezone # pythonだとdatetime.nowで現在日時&時刻を取得できるが、djangoはtimezone.nowという独自の機能がある

class Day(models.Model):
  # id = models.AutoField(primary_key=True) # 更新の際にprimary_keyを内部的に生成している。AutoFieldは1,2,3,4と順に作成する(この記述がなくてもdjangoが自動的に生成してくれる)
  title = models.CharField('タイトル', max_length=200)
  text = models.TextField('本文')
  date = models.DateTimeField('日付', default=timezone.now)

  def __str__(self):
    return self.title