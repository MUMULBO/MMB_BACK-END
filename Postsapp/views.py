from tkinter.messagebox import NO
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Posts    
from .serializers import PostSerializer, CommentSerializer
from django.db.models import Q
from .models import Posts
from django.core import serializers

def home(request):
    return(request, 'Postsapp/index.html')

class Postclass(APIView):    
    def get(self, request):
        #검색어와 전공이 들어온다면
        get_major_id=request.GET.get('major_id')
        get_keyword=request.GET.get('keyword')
        if get_major_id != '':
            searchposts=Posts.objects.all().filter(Q(title__contains=get_keyword)&
            Q(major_id__id__contains=get_major_id)).order_by('-created_time')                          
            if request.GET['point']: 
                searchposts=Posts.objects.all().filter(Q(title__contains=get_keyword)&
            Q(major_id__id__contains=get_major_id)).order_by('-created_time')
            serializer = PostSerializer(searchposts, many=True)
            return Response(serializer.data)            
        #검색어와 전공이 들어오지 않는다면          
        else:
            #point 값이 넘어오면 포인트순 정렬               
            if request.GET['point'] == 'True':              
                Post = Posts.objects.all().order_by('-post_point')
            #point 값이 넘어오지 않으면 최신순 정렬
            else:
                Post = Posts.objects.all().order_by('-created_time')
            serializer = PostSerializer(Post, many=True)            
            return Response(serializer.data)

    # 새로운 Post 글을 작성할 때
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Post의 detail을 보여주는 역할
class Postdetail(APIView):
    # Blog 객체 가져오기
    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            raise Http404
    
    # Post의 detail 보기
    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    # Post 수정하기
    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data) 
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Blog 삭제하기
    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class Commentclass(APIView):        
    def post(self, request):
        # request.data는 사용자의 입력 데이터
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid(): #유효성 검사
            serializer.save() # 저장
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# {
#      “description” : 내용
#      “post_id” : 게시물 아이디
#      “image_src” : 리사이징된 이미지
#      “is_anony” : 익명 여부(boolean)
#      “token” : 유저 토큰
# }
