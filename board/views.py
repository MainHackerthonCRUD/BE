from django.shortcuts import render
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from .models import Board
from rest_framework.response import Response
from .serializers import BoardListSerializer, BoardDetailSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .permissions import IsOwnerOrReadOnly

from .serializers import *
import json

file_path='C:/Users/user/Desktop/hackerthon05/hospital_list_withGU.json'
with open(file_path, 'r', encoding='utf-8') as file:
    datas = json.load(file)


datasave=[]

# board/post/
@api_view(['GET'])
def board_post(request):
    if request.method=='GET':
        for data in datas:
            tempdata={}
            for i in data:
                if i=='병원명':
                    tempdata['hospital_name']=data[i]
                elif i=='주소':
                    tempdata['address']=data[i]
                elif i=='구':
                    tempdata['gu']=data[i]
                elif i=='예약가능여부':
                    tempdata['reservation']=data[i]

                elif i=='방문자리뷰':
                    tempdata['visitcnt']=data[i].split()[2]
                    if ',' in tempdata['visitcnt']:
                        tempdata['visitcnt']=tempdata['visitcnt'].replace(',',"")

                elif i=='블로그리뷰':
                    try:
                        tempdata['blogcnt']=data[i].split()[2]
                        if ',' in tempdata['blogcnt']:
                            tempdata['blogcnt']=tempdata['blogcnt'].replace(',',"")
                            # 1000번대가 존재하는지 확인
                    except:
                        tempdata['blogcnt']=None


                elif i=='산부인과전문의수':
                    try:
                        tempdata['maindoctorcnt']=data[i].split()[1].replace('명','')
                    except:
                        tempdata['maindoctorcnt']=None

            serializer=BoardPostSerializer(data=tempdata)
            if serializer.is_valid():
                # post=serializer.save(user=request.user)
                serializer.save(user=request.user)
                
            # datasave.append(tempdata)
        return None
# post=serializer.save(user=request.user)



    for i in datasave:
        for j in i:
            if j=='hospital_name':
                print(i[j])

        # serializer=BoardPostSerializer(data=request.data)
        # return data

'''
{'병원명': '우아한여성의원', 
'주소': '서울 강남구 신사동', 
'구': '강남구', 
'예약가능여부': '예약', 
'진료시작시각': '10:00에 진료 시작', 
'방문자리뷰': '방문자 리뷰 275', 
'블로그리뷰': '블로그 리뷰 656', 
'산부인과전문의수': '산부인과전문의\xa02명', 
'기타전문의여부': None},

'''
'''
병원명
주소
구
예약가능여부
진료시작시각
방문자리뷰
블로그리뷰
산부인과전문의수
기타전문의여부

'''






# board/home/
@api_view(['GET']) 
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticatedOrReadOnly])
def board_list(request):
    if request.method =='GET':
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


    # elif request.method == 'POST':
    #     serializer = BoardDetailSerializer(data=request.data)

    #     if serializer.is_valid():
    #         board = serializer.save(user = request.user)
    #         result = BoardDetailSerializer(board)
    #         return Response(result.data, status = status.HTTP_201_CREATED)
    #     return Response(status=status.HTTP_400_BAD_REQUEST)   
    



'''
한 블로그 조회
'''
# board/home/<int:pk>/
@api_view(['GET','PUT','DELETE'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsOwnerOrReadOnly])
def board_detail(request, pk):
    try: 
        board = Board.objects.get(pk=pk)
        if request.method == 'GET':
            serializer = BoardDetailSerializer(board)
            return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method =='PUT':
            serializer = BoardDetailSerializer(board, data=request.data)
            if serializer.is_valid():
                board = serializer.save(user = request.user)
                result = BoardDetailSerializer(board)
                return Response(result.data,status=status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        elif request.method =='DELETE':
            board.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
    except Board.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)


# 리뷰 작성
@api_view(['POST'])
def review_post(request,pk):
    if request.method=='POST':
        post=Board.objects.get(pk=pk)
        serializer=CommentRequestSerializer(data=request.data)
        flag=True
        if serializer.is_valid():
            comment=serializer.save(board=post,user=request.user)
            # if flag:
            #     print(request.user)
            response=CommentResponseSerializer(comment)
            return Response(response.data,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

'''
리뷰 저장할 때 user=request.user로 연결해서 저장했음
근데 유저 통해서 리뷰 불러오려고 하면 연결이 안 돼있는 것 같음
확인할 것.
모든 데이터 다 지우거나 리뷰 데이터 뭐 있는지 확인하거나 해야할 듯
유저 많이 지워서 지금 존재하는 유저 id 확인해서 pk 수정해서 접속해볼 것
'''
    
    
'''
comment=serializer.save(board=post)
save() 메서드 내부 작동 방식

- serializer.save() 메서드가 호출되면, 기본적으로 create 메서드가 호출되어
새로운 Comment 인스턴스가 생성됨
'''
'''
{
"title":"sfds",
"body":"dsf",
"star":"sdf"
}

'''
'''
class MypageSerializer(serializers.ModelSerializer):
    
    comments=MypageCommentSerializer(many=True,read_only=True)

    class Meta:
        model=CustomUser
        fields=['nickname','comments']
'''
# 마이페이지
# board/mypage/
@api_view(['GET'])
def mypage(request,pk):
    if request.method=='GET':
        user=CustomUser.objects.get(nickname='hongddd')
        # pk값 뭐로 할 지 생각하고 수정하기
        serializer=MypageSerializer(user)
        return Response(serializer.data,status=status.HTTP_200_OK)


 


# 구에 따라 분류
@api_view(['GET'])
def find_gu(request,gu):
    if request.method=='GET':
        locations=Board.objects.filter(gu=gu)
        serializer=GuSerializer(locations,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)





 







# 일단 제외
@api_view(['GET'])
def board_region(request, region):
        boards = Board.objects.filter(region__contains=region)
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def board_name(request, name):
    boards = Board.objects.filter(hospital_name__contains=name)
    serializer = BoardListSerializer(boards, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)