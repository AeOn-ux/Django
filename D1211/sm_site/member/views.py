from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse
from . models import Member


# 로그인
def login(request):
    if request.method == 'GET':
        # 쿠키 읽기
        cook_id = request.COOKIES.get("cook_id","")
        context = {"cook_id":cook_id}
        return render(request, 'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        cook_keep = request.POST.get("cook_keep")
        
        print("post 입력 : ",id,pw)
        qs = Member.objects.filter(id=id,pw=pw)
        # qs = Member.objects.get(id=id,pw=pw).DoesNotExist() # 
        
        # get() -> 하나의 객체, 단일 객체일때만 사용 가능 -> 고유 id, 유니크한 이메일 등
        # filter() -> 여러 객체, 0개 이상 가능 -> 리스트 형태로 조회 가능하다.
        if qs:
            print("아이디와 비밀번호가 일치합니다.")
            # 섹션 저장
            # [키] = 깂
            request.session['session_id'] = id
            
            context = {"error":"1"}
            response = render(request,'member/login.html',context)
            
            # 쿠키 저장, 삭제
            if cook_keep:
                response.set_cookie("cook_id",id,max_age=60*60*24*30)
            else:
                response.delete_cookie("cook_id") # 쿠키 삭제
            return response
        else:
            print("아이디와 비밀번호가 일치하지 않습니다.")
            context = {"error":"0"}
            return render(request,'member/login.html',context)
        
        
def logout(request):
    # 섹션 삭제
    request.session.clear() # 섹션 모두 삭제
    context = {"error":"-1"}
    return render(request,'member/login.html',context)
    

# 회원 전체리스트 페이지
def list(request):
    qs = Member.objects.all().order_by('-mdate')
    context = {"list":qs}
    return render(request, 'member/list.html',context)


# 회원등록페이지
def write(request):
    if request.method == 'GET':
        return render(request,'member/write.html')
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        gender = request.POST.get("gender")
        hobby = request.POST.getlist("hobby")
        
        # Member.objects.create(
        #     id=id, pw=pw, name=name, phone=phone, gender=gender, hobby=hobby
        # ) # 중복 불가 함수
        
        qs = Member(id=id, pw=pw, name=name, phone=phone, gender=gender, hobby=hobby)
        qs.save()
        
        
        print("post 확인 :")
        return redirect('/')