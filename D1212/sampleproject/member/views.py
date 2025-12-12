from django.shortcuts import render, redirect
from. models import Member

# 로그인 부분
def login(request):
    if request.method == 'GET':
        # 쿠키 읽어와서 context 저장해서 전송
        cook_id = request.COOKIES.get('cook_id','') # 없으면 빈 공백 전송
        context = {'cook_id':cook_id}
        
        return render(request,'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        login_keep = request.POST.get("login_keep")
        # id,pw를 활용해서 로그인체크
        qs = Member.objects.filter(id=id,pw=pw)
        
        if qs:
            print("id,pw 일치 : ",id,pw)
            # session 저장
        
            request.session['session_id'] = id
            request.session['session_name'] = qs[0].name
            context = {"state_code":"1"}
            response= render(request,'member/login.html',context)
            #쿠키 저장
            if login_keep:
                response.set_cookie('cook_id',id)
            #쿠키 삭제
            else:
                response.delete_cookie("cook_id")
        
        else:
            print("id,pw 불일치")
            context = {"state_code":"0"}
            response= render(request,'member/login.html',context)
        
        
    return response


# 로그아웃 부분
def logout(request):
    # 섹션 모두 삭제
    request.session.clear()
    context = {"state_code":"-1"}
    return render(request,'member/login.html',context)