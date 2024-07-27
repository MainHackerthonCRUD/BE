from django.urls import path
from .views import *
from . import views

app_name = 'board'

urlpatterns = [
    # 전체 병원 리스트 조회
    path('home/', board_list),

    # 병원 데이터 저장 - 한번만 실행/접속
    path('post/',board_post),
    
    # 병원 객체 조회
    path('home/<int:pk>/',board_detail),

    # 병원 객체에 대해 리뷰 작성
    path('home/<int:pk>/comments/',review_post),

    # mypage
    path('mypage/<int:pk>/',mypage),


    # 구 종류
    path('<str:gu>/',find_gu),




    # # 지역별 병원 조회
    # path('region/<str:region>/', board_region),


    # path('name/<str:name>/',board_name)

]