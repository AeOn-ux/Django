from django.shortcuts import render

# Create your views here.
def index(request): 
    # 쿠키 검색(읽어오기) - request
    # 쿠키 저장 - reponse
    
    # 쿠키 검색
    cook_info = request.COOKIES
    print("쿠키 모든 정보 :", cook_info)
    cook_id = request.COOKIES.get("cook_id","") # cook_id, 없을 때 빈공백 처리    
    print("cook_id 정보 : ", cook_id)
    
    response = render(request,'index.html')
    # 쿠키 저장 - response
    # cook_id = aaa
    # 유지시간 없으면, 브라우저 종료 시 사라진다. 시간을 설정하면 시간동안 유지 가능.
    
    # 쿠키 정보가 없을 때만 쿠키 저장
    # if not cook_id:
    #     response.set_cookie("smsite_connect","ok")
    #     response.set_cookie("ip","127.0.0.1:8000",max_age=60*60*24) # 초*분*시(*일)
    # else:print("쿠키를 저장하지 않습니다.")
        
    return response
    
    
    