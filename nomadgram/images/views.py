
#from django.shortcuts import render
# Create your views here.

from rest_framework.views import APIView
from rest_framework.response import Response
from . import models , serializers

class ListAllImages(APIView):
    
    def get(self, request , format=None):
        
        all_images = models.Image.objects.all()  #이미지를 디비로부터 불러온다 

        serializer = serializers.ImageSerializer(all_images, many=True)  #그 이미지를 시리얼라이저로 만든다. 

        return Response(data=serializer.data)

class ListAllComments(APIView):
    def get(self, request, format=None) :
        all_comments = models.Comment.objects.all()

        serializer = serializers.CommentSerializer(all_comments, many=True)
        return Response(data=serializer.data)

class ListAllLikes(APIView):
    def get(self, request, format=None):
        all_likes = models.Like.objects.all()
        serializer = serializers.LikeSerializer(all_likes, many=True)
        return Response(data=serializer.data)







