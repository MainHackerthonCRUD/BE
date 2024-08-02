from django.urls import path
from .views import *
from . import views

app_name = 'board'

'''
{
"title":"test",
"body":"test",
"star":3
}
{
"username":"honggyu",
"password1":"asdf1234qwer",
"password2":"asdf1234qwer",
"nickname":"hongddd"
}
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNjA3MDk5LCJpYXQiOjE3MjI2MDM0OTksImp0aSI6Ijg0ZDM3MmFjMTY1NDQ2ZjdhOTgwNGQxZmJlOWZiNDRmIiwidXNlcl9pZCI6MzN9.H0ZfzwOKpBax8SxB6ANzE0w_KcYmd3XcgPq3pFRNSI0

# 댓글
{
    "id": 19,
    "nickname": "hongddddddd",
    "title": "test",
    "body": "test",
    "created_at": "2024-08-02",
    "star": "3"
}
'''

urlpatterns = [
    # json 파일 저장
    # path('savejson/',board_post),
    # 오류 생겨서 주석처리 해놨습니다.

    
    

# 병원
    # 전체 병원 리스트 조회 - OK
    path('home/', board_list),

    
    
    # 병원 이름 검색 - OK
    path('search/<str:name>/', hospital_name),

    # 병원 구 검색 - OK
    path('searchgu/<str:gu>/',hospital_gu),

    

# 리뷰
    # 병원 객체에 대해 리뷰 작성 - OK
    path('<int:pk>/comment/',comment_post),

    # 병원 id 값에 달린 댓글 가져오기 - OK
    path('<int:pk>/commentget/', comment_list),

    
    # 리뷰 객체 get, put,delete
    path('review/<int:board_pk>/<int:comment_pk>/',review_put_delete),



# 마이페이지
    # mypage - OK
    path('mypage/<str:pk>/',mypage),




    # mypage -> review put
    path('reviewput/<int:comment_pk>/',review_put),

    # mypage -> review delete
    path('reviewdelete/<int:comment_pk>/',review_delete),
    













# etc
    # 병원 객체 조회
    # 프론트 필요 없음
    path('hospital/<int:pk>/',board_detail),

    # 임시로 만든 병원 전체 POST
    # path('homehonggyu/',board_post),

    # 병원 데이터 저장 - 한번만 실행/접속
    path('post/', data_post,),


    # 필요 없어짐
    # 개별 리뷰 페이지 - OK
    path('review/<int:pk>/',review_get),
    # id : 14 -> 삭제됨
]