from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from.models import Student



# 학생 등록 페이지
def write(request):
    if request.method == 'GET':
        return render(request,'student/write.html')
    elif request.method == 'POST':
        
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        
        # Student db 저장
        qs= Student(name=name, age=age, grade=grade, gender=gender, hobby=hobby)
        qs.save()
        
        print("post확인 : ", name)
        return redirect(reverse('student:list')) # 바뀐 페이지에서도 주소값을 바꿔줌.
        # reverse ('student:list')을 찾아갈 수 있게하는 명령어
        # return render(request,'student/list.html') # 페이지만 열어주고 주소값이 바뀌지는 않음
    
# 학생리스트페이지   
def list(request):
    qs = Student.objects.all().order_by('-sno')
    context = {'list':qs}
    return render(request,'student/list.html',context)

# 학생 상세보기페이지
def view(request,sno):
    qs = Student.objects.get(sno=sno)
    context = {'stu':qs}
    return render(request,'student/view.html',context)

# 학생 삭제 페이지
def delete(request,sno):
    qs = Student.objects.get(sno=sno)
    qs.delete()
    return redirect(reverse('student:list'))
    
# 학생 수정 페이지
def update(request,sno):
    if request.method == 'GET':
        qs = Student.objects.get(sno=sno)
        context = {"stu":qs}
        return render(request,'student/update.html',context)
    elif request.method == 'POST':
        
        name = request.POST.get("name")
        age = request.POST.get("age")
        grade = request.POST.get("grade")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        
        # Student db 저장
        qs = Student.objects.get(sno=sno)
        qs.name = name
        qs.age = age
        qs.grade = grade
        qs.gender = gender
        qs.hobby = hobby # 수정되면 항목 추가 말고 수정된 값으로 항목을 변경해라.
        # qs= Student(name=name, age=age, grade=grade, gender=gender, hobby=hobby) # 항목 추가
        qs.save()
        
        print("post확인 : ", name)
        return redirect(reverse('student:list')) # 바뀐 페이지에서도 주소값을 바꿔줌.
        # reverse ('student:list')을 찾아갈 수 있게하는 명령어
        # return render(request,'student/list.html') # 페이지만 열어주고 주소값이 바뀌지는 않음