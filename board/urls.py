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
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNTE2MzkzLCJpYXQiOjE3MjI1MTI3OTMsImp0aSI6IjEzMmY4OTJhYjRjZTQwNjZiOGFiODYzYmE1YzUwZTE5IiwidXNlcl9pZCI6MX0.nMF5mxGfojVQr4i3ugqWgSZBm04v6JO14hdaZVT7I-o",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTcyMjU5OTE5MywiaWF0IjoxNzIyNTEyNzkzLCJqdGkiOiJjZDc0MWJjMDZiNDE0Yzk5OTM2MDBjN2FjZGU5ZDVjNSIsInVzZXJfaWQiOjF9.lphmChStwnA-LpC1BRGSsioyXrxHz07FlzyY1wqQbIo",
    "user": {
        "id": 1,
        "username": "honggyu",
        "password": "pbkdf2_sha256$720000$pxmEvSPDgrdZwPE6m46yoG$6Kpdw16Chx2hzzLwtEX3uBoetCTbsE/3wZHQV5RFNrM=",
        "nickname": "hongddd"
    }
}
로컬
eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNDk1MzY4LCJpYXQiOjE3MjI0OTE3NjgsImp0aSI6Ijk3NzkwYjJmNGE4MTQ0NzhhMGE1ZDc2NzhmOWE5MmY5IiwidXNlcl9pZCI6OH0.0I5UhBAH727jHahf0XKmmr4ihAvh7Eq3kPSvg1Opago
# 서버
Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzIyNTE1NDc0LCJpYXQiOjE3MjI1MTE4NzQsImp0aSI6ImFiZGZiODYyM2MzYzRiYjM5ZDlmZDRjZmVkMWMzNzc3IiwidXNlcl9pZCI6NX0.sD7CHWoFf_WH0m6HbcQ6-AjvVyi8nCdM49lyg4flewI

{
    "id": 23,
    "nickname": "hongddd",
    "title": "test",
    "body": "test",
    "created_at": "2024-08-01",
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