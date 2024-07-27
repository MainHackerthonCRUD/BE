from rest_framework import serializers
from .models import *


'''
class BoardDetailSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    comments=CommentResponseSerializer(many=True,read_only=True)
    class Meta:
        model = Board
        fields = ['id','hospital_name','address','comments']
    # def get_user(self, obj):
    #     return obj.user.nickname
'''

# mypage
from member.models import CustomUser

class MypageCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields=['title','date','star']


from django.db.models import Avg,Sum

# user로부터 comment 역참조
class MypageSerializer(serializers.ModelSerializer):

    comments=MypageCommentSerializer(many=True,read_only=True)

    comments_count=serializers.SerializerMethodField()
    star_average=serializers.SerializerMethodField()

    class Meta:
        model=CustomUser
        fields=['nickname','comments','comments_count','star_average']
    
    def get_comments_count(self,obj):
        return obj.comments.count()
    
    def get_star_average(self,obj):
        avg_star=obj.comments.aggregate(Avg('star')).get('star__avg')
        return avg_star if avg_star is not None else 0
        



# gu 시리얼라이저
class GuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Board
        fields=['id','hospital_name','address','gu','reservation','visitcnt','blogcnt',
                'maindoctorcnt']
       




        

# json으로부터 병원 객체 저장
class BoardPostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Board
        fields=['id','hospital_name','address','gu','reservation','visitcnt','blogcnt',
                'maindoctorcnt']


# 병원 객체 리스트 보여주기
class BoardListSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()

    class Meta:
        model = Board
        fields = ['id','hospital_name', 'address','gu','reservation','visitcnt','blogcnt',
                'maindoctorcnt']
    # def get_user(self, obj):
    #     return obj.user.nickname


'''
class Comment(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    board=models.ForeignKey(Board, null=True,on_delete=models.CASCADE,
                            related_name='comments')

    title=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    star=models.IntegerField()  # 나중에 다시 확인
'''


from .models import Comment
from django.utils import timezone

# Comment 가져오기
class CommentResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    nickname=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['nickname','title','body','star','created_at']

    def get_nickname(self,obj):
        return obj.user.nickname if obj.user else 'Anonymous'

    def get_created_at(self,obj):
        # get_형식으로 설정해야 함.
        # db는 안 바뀌고 클라이언트한테 보낼 때만 바뀜.
        time=timezone.localtime(obj.date)
        return time.strftime('%Y-%m-%d')

# self : 현재 CommentResponseSerializer의 인스턴스를 참조함.
#       이를 통해 인스턴스의 다른 메서드나 속성에 접근할 수 있음
# obj : 직렬화할 Comment 모델 인스턴스를 나타냄.
#       이 인스턴스를 통해 Comment 객체의 속성에 접근할 수 있음.


# board/home/<int:pk>/
# 병원 객체 선택
class BoardDetailSerializer(serializers.ModelSerializer):
    # user = serializers.SerializerMethodField()
    comments=CommentResponseSerializer(many=True,read_only=True)
    class Meta:
        model = Board
        fields = ['id','hospital_name','address','comments']
    # def get_user(self, obj):
    #     return obj.user.nickname

# read_only=True를 설정하면 직렬화 응답에서만 사용되고 입력되는 것을 방지할 수 있음.




'''
class Comment(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    board=models.ForeignKey(Board, null=True,on_delete=models.CASCADE,
                            related_name='comments')

    title=models.CharField(max_length=100)
    body=models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)
    star=models.IntegerField()  # 나중에 다시 확인
'''


# 리뷰 작성
# 리뷰 저장
class CommentRequestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Comment
        fields=['title','body','star']

# 리뷰 반환
class CommentResponseSerializer(serializers.ModelSerializer):
    created_at=serializers.SerializerMethodField()
    nickname=serializers.SerializerMethodField()
    class Meta:
        model=Comment
        fields=['nickname','title','body','created_at','star']

    def get_created_at(self,obj):
        # db는 안 바뀌고 클라이언트한테 보낼 때만 바뀜.
        time=timezone.localtime(obj.date)
        return time.strftime('%Y-%m-%d')
    def get_nickname(self,obj):
        nickname=obj.user.nickname
        return nickname

    
    
    
    '''
{
"title":"sdf",
"body":"sdf",
"star":3
}
    '''
    