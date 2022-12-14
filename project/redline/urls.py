from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from redline import views
from rest_framework_simplejwt import views as jwt_views
import json
import requests

urlpatterns = [
    path('Users/', views.UserList.as_view()),
    path('Users/<int:pk>', views.UserDetail.as_view()),

    path('Posts/', views.PostList.as_view()),
    path('Posts/<int:pk>', views.PostDetail.as_view()),

    path('PostReplies/', views.PostReplyList.as_view()),
    path('PostReplies/<int:pk>', views.PostReplyDetail.as_view()),

    path('PostLikes/', views.PostLikeList.as_view()),
    path('PostLikes/<int:pk>', views.PostLikeDetail.as_view()),

    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),

    path('Following/', views.IsFollowingList.as_view()),
    path('Following/<int:pk>', views.IsFollowingDetail.as_view()),

    path('Vehicles/', views.VehiclesList.as_view()),
    path('Vehicles/<int:pk>', views.VehiclesDetail.as_view()),


    path('cars/', views.get_cars),
]

urlpatterns = format_suffix_patterns(urlpatterns)