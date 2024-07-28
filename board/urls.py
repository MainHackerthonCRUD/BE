from django.urls import path
from .views import *
from . import views

app_name = 'board'

urlpatterns = [
    # 전체 병원 리스트 조회
    path('home/', board_list),

    # 병원 데이터 저장 - 한번만 실행/접속
    path('post/', data_post,),
    
    # 병원 객체 조회
    path('<int:pk>/',board_detail),

    # 병원 객체에 대해 리뷰 작성
    path('<int:pk>/comment/',comment_post),

    # mypage
    #path('mypage/<int:pk>/',mypage),

    # 병원 이름 검색
    path('search/<str:name>/', hospital_name),

    # 구 검색
    path('search/<str:gu>/',hospital_gu),



]