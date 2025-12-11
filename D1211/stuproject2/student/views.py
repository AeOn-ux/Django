from django.shortcuts import render, redirect # 화면에 html을 보여주고(render), 페이지 이동(redirect)
from django.urls import reverse # reverse -> 앱 이름으로 불러오기

from django.http import HttpResponse # html 파일이 없어도 url이 잘 연결되었나 확인이 필요할 때 사용.
from . models import Student # models 파일의 Student 함수 사용


# html 파일에서는 method=post 또는 method=get 가능하지만
# py 즉, python 파일에서는 꼭 대문자로 표기. method=POST or method=GET



# Create your views here.
# 학생 등록 페이지 -> 데이터 저장의 의미
def write(request):
    if request.method == 'GET': # GET은 주소창/링크로 접근
        return render(request,'student/write.html')
    elif request.method == 'POST': # POST는 폼 데이터 전송
        
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby") # 복수선택이니 list로 여러값을 출력할 수 있게 getlist
        
        # Student db 저장
        qs= Student(name=name, age=age, grade=grade, gender=gender, hobby=hobby)
        qs.save()
        
        print("post 확인 : ", name)
        return redirect(reverse('student:list'))# 바뀐 페이지에서도 주소값을 바꿔줌.
        # reverse ('student:list')을 찾아갈 수 있게하는 명령어
        # return render(request,'student/list.html') # 페이지만 열어주고 주소값이 바뀌지는 않음

# 학생 리스트 페이지
def list(request):
    return render(request,'student/list.html')
    
