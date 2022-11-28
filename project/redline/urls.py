from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from redline import views

urlpatterns = [
    path('Users/', views.UserList.as_view()),
    path('Users/<int:pk>', views.UserDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)