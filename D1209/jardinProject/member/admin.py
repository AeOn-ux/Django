from django.contrib import admin
# Member 앱에서 models 파일 안에 Member 클래스 가져옴
from member.models import Member


admin.site.register(Member)

qs = Member(id='eee',pw='1111',name='김 구',age=22,phone='010-1111-1111',gender='남성',hobby='조깅')
qs.save()