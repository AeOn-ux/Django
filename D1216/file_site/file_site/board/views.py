from django.shortcuts import render

# 게시글 작성
def write(request):
    return render(request,'board/write.html')
