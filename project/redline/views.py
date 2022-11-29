from rest_framework import generics, status
from redline.models import CustomUser, Is_following, Posts, Post_likes, Post_reply
from redline.serializers import UserSerializer, IsFollowingSerializer, PostSerializer, PostReplySerializer, PostLikesSerializer

class UserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class PostList(generics.ListCreateAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer

class PostReplyList(generics.ListCreateAPIView):
    queryset = Post_reply.objects.all()
    serializer_class = PostReplySerializer

class PostReplyDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_reply.objects.all()
    serializer_class = PostReplySerializer

class PostLikeList(generics.ListCreateAPIView):
    queryset = Post_likes.objects.all()
    serializer_class = PostLikesSerializer

class PostLikeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_likes.objects.all()
    serializer_class = PostLikesSerializer

class IsFollowingList(generics.ListCreateAPIView):
    queryset = Is_following.objects.all()
    serializer_class = IsFollowingSerializer

class IsFollowingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Is_following.objects.all()
    serializer_class = IsFollowingSerializer