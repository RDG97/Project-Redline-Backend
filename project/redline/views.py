from rest_framework import generics, status
from redline.models import CustomUser, Is_following, Posts, Post_likes, Post_reply
from redline.serializers import UserSerializer, IsFollowingSerializer, PostSerializer, PostReplySerializer, PostLikesSerializer
import json
import requests
from django.http import HttpResponse
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


#f"https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make=ford&model=fiesta&year={}"

def get_cars(request):
    make = request.GET.get("make")
    model = request.GET.get("model")
    year = request.GET.get("year")
    print(make)
    url = f"https://www.carqueryapi.com/api/0.3/?callback=?&cmd=getTrims&make={make}&model={model}&year={year}"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    response = requests.get(url, headers = headers)
    print(dir(response))
    print(response.text)
    data = response.text
    print(data[2:-2])
    # sorted_data = sorted(data, key=lambda k: k["id"], reverse=False)
    # page_num = request.GET.get("page", 1)
    # paginator = Paginator(sorted_data, 25)
    # try:
    #     page_obj = paginator.page(page_num)
    # except PageNotAnInteger:
    #     page_obj = paginator.page(1)
    # except EmptyPage:
    #     page_obj = paginator.page(paginator.num_pages)
    # result_list = list(page_obj)
    return HttpResponse(json.dumps(data[2:-2]), content_type="application/json")