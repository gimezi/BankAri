from django.contrib import admin
from django.urls import path, include
from . import urls

urlpatterns = [
    path('admin/', admin.site.urls),

    # 로그인
    path('accounts/', include('dj_rest_auth.urls')),
    path('accountsapps/', include('accounts.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
    
    # 게시판
    path('api/v1/', include('articles.urls')),

    # 환율 계산기
    path('exchange/', include('exchanges.urls')),

    # 예/적금 데이터
    path('bankings/', include('bankings.urls')),

     # 추천 
    path('recommends/', include('recommends.urls'))
]
