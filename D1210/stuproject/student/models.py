from django.db import models

# Create your models here.
# 테이블 생성 - 파이썬 명령어로 sql 구문을 대체
# 테이블명 student_student 생성됨
class Student(models.Model):
    sno = models.AutoField(primary_key=True) # 테이블을 생성하면 항상 id - AutoField 생성이 됨.
    name = models.CharField(max_length=100) # name varchar2(100),
    age = models.IntegerField(default=0) 
    grade = models.IntegerField(default=1)
    gender = models.CharField(max_length=10) # gender char(1),
    hobby = models.CharField(max_length=100,default='게임') # hobby varchar2(100)
    
    # id = models.CharField(max_length=100,primary_key=True) # id VARCHAR2(100) primary key,
    # pw = models.CharField(max_length=100) # pw varchar2(100) not null,
    # phone = models.CharField(max_length=13) # phone char(13),
    # hobby = models.CharField(max_length=100) # hobby varchar2(100)

    # qs = Student(sno='1',name='홍길동',age=20,grade='1',gender='남성')
    # Student.objects.create(sno='1',name='홍길동',age=20,grade='1',gender='남성')

    # 객체출력 - 주소값, __str__ 객체를 문자열로 출력시켜줌.
    def __str__(self):
        return f"{self.sno},{self.name},{self.age},{self.grade},{self.gender}"
    # def __str__(self):
    #     return f"{self.sno},{self.name},{self.age}"