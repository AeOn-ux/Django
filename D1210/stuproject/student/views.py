from django.shortcuts import render,redirect
from django.urls import reverse
from . models import Student



# 학생 등록 함수
# Create your views here.
def write(request):
    if request.method == 'GET': # get 방식
        return render(request,'student/write.html')
    elif request.method == 'POST': # post 방식
        # form 폼에서 넘어온 데이터 처리
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        # hobbys = ','.join(hobby) # 리스트 타입을 문자열 타입으로 변환 방법
        # 리스트 타입을 문자열 항목에 저장하면 자동으로 형변환이 된다.
        qs = Student(name=name, age=age, grade=grade, gender=gender, hobby=hobby)
        qs.save()
        
                
        print("이름 :",name)
        print("나이 :",age)
        print("학년 :",grade)
        print("성별 :",gender)
        print("취미 :",hobby)
        
        
        return redirect(reverse('student:list'))
        # return redirect('/student/list/')
        # redirect : 보내다. 이동시키다.라는 함수
    
# 학생 리스트 함수
# Create your views here.
def list(request):
    # db 명령어 - select, insert, update, delete
    qs = Student.objects.all()
    qs = Student.objects.all().order_by('-sno','name')
    context = {"name":"2025","list":qs}
    return render(request,'student/list.html', context)

# 학생 상세 보기 함수
def view (request,sno):
    print("넘어온 데이터 sno : ",sno)
    qs = Student.objects.get(sno=sno)
    context = {"student":qs}

    return render(request,'student/view.html', context)


# 학생 리스트 함수
def delete(request):
    return render(request,'student/delete.html')