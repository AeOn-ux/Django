from django.db import models

# Create your models here.
# 테이블 생성 - 파이썬 명령어로 sql 구문을 대체
class Student(models.Model):
    id = models.CharField(max_length=100,primary_key=True) # id VARCHAR2(100) primary key,
    pw = models.CharField(max_length=100) # pw varchar2(100) not null,
    name = models.CharField(max_length=100) # name varchar2(100),
    age = models.IntegerField(default=0) 
    phone = models.CharField(max_length=13) # phone char(13),
    gender = models.CharField(max_length=10) # gender char(1),
    hobby = models.CharField(max_length=100) # hobby varchar2(100)



    # 객체출력 - 주소값, __str__ 객체를 문자열로 출력시켜줌.
    def __str__(self):
        return f"{self.id},{self.name},{self.age},{self.gender}"