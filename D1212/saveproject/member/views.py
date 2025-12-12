from django.shortcuts import render, redirect

# Create your views here.
def login(request):
    if request.method == 'GET':
        # 저장된 아이디 띄우기 - > 쿠키 불러오기
        cook_id = request.COOKIES.get("cook_id","")
        context = {"cook_id":cook_id}
        return render(request, 'member/login.html',context)
    elif request.method == 'POST':
        id = request.POST.get("id")
        pw = request.POST.get("pw")
        login_keep = request.POST.get("login_keep")
        
        # 쿠키 읽기
        print("모든 쿠키 읽기 : ",request.COOKIES)
        
        
        # 쿠키 저장
        response = redirect('/') 
        
        if login_keep:
            print("쿠키 저장")
            response.set_cookie("cook_id",id)
        else:
            print("쿠키 삭제")
            response.delete_cookie("cook_id")
        print("post 입력된 데이터 : ",id,pw,login_keep)
        
        
        return response
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # if request.method == 'GET':
    #     # 쿠키 검색
    #     cooksave_id = request.COOKIES.get("cooksave_id","") # 읽어오는 명령어
    #     context = {"cooksave_id":cooksave_id}
    #     return render(request,'member/login.html',context)
    # elif request.method == 'POST':
    #     id = request.POST.get("id")
    #     pw = request.POST.get("pw")
    #     login_keep = request.POST.get("login_keep") # getlist()
        
    #     # 쿠키저장
    #     response = redirect("/")
    #     if login_keep:
    #         print("아이디 저장이 완료되었습니다.")
    #         ## 쿠키에 아이디를 저장시켜줌.
    #         response.set_cookie("cooksave_id", id, max_age=60*60*24*30)
            
    #     else:
    #         print("아이디 저장 X")
        
    #     return response