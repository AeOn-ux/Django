from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt



def index(request):
    return render(request,'main.html')

def chart1(request):
    return render(request,'chart1.html')

def chart2(request):
    return render(request,'chart2.html')

# # @csrf_exempt # csrf_token 예외처리
# def chart_json(request):
#     context = {'dd_data':[10, 5, 9, 8, 3, 6],'ll_data':['홍길동','유관순','이순신','강감찬','김구','김유신']}
#     return JsonResponse(context)

from home.models import ChartData

def chart2_json(request):
    qs = ChartData.objects.all()
    l_qs = list(qs.values())
    
    context = {'cc_year':['2020', '2021', '2022', '2023', '2024', '2025'],'cc_data':[12, 15, 13, 16, 20, 21]}
    
    return JsonResponse(context)