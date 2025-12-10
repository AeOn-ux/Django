from django.db import models


class Stuscore(models.Model):
    sno = models.AutoField(primary_key=True) # 테이블을 생성하면 항상 id - AutoField 생성이 됨.
    name = models.CharField(max_length=100) # name varchar2(100),
    kor = models.IntegerField(default=0)
    eng = models.IntegerField(default=0)
    math = models.IntegerField(default=0)
    total = models.IntegerField(default=0)
    avg = models.FloatField(default=0)

    # qs = Stuscore(sno='1',name='홍길동',age=20,grade='1',gender='남성')
    # Stuscore.objects.create(sno='1',name='홍길동',age=20,grade='1',gender='남성')

    # 객체출력 - 주소값, __str__ 객체를 문자열로 출력시켜줌.
    def __str__(self):
        return f"{self.sno},{self.name},{self.total},{self.avg}"
