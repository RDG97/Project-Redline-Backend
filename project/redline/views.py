from rest_framework import generics, status
from redline.models import CustomUser, Is_following, Posts, Post_likes, Post_reply, Vehicles
from redline.serializers import UserSerializer, IsFollowingSerializer, PostSerializer, PostReplySerializer, PostLikesSerializer, VehicleSerializer
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

class VehiclesList(generics.ListCreateAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer

class VehiclesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicles.objects.all()
    serializer_class = VehicleSerializer


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
    return HttpResponse(json.dumps(data[2:-2]), content_type="application/json")