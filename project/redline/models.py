from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_banned = models.BooleanField(default=0)
    filter_explicit = models.BooleanField(default=0)
    screen_name = models.CharField(max_length=25, default='')
    bio = models.CharField(max_length=150, default='')
    profile_pic = models.URLField(default="https://kasmanninsurance.com/wp-content/uploads/2015/10/Car_with_Driver-Silhouette.svg-red.png")
    bgImage = models.URLField(default='')
    class Meta:
        ordering = ['id']
    def __str__(self):
        return self.username

class Is_following(models.Model):
    id = models.AutoField(primary_key=True)
    follower = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='follower')
    followed = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='following')
    class Meta:
        ordering = ['id']



class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text_content = models.CharField(max_length=200, default='')
    media_link = models.URLField(default='', blank=True)
    created_at = models.DateTimeField()
    explicit = models.BooleanField(default=0)
    class Meta:
        ordering = ['id']

class Post_reply(models.Model):
    id = models.AutoField(primary_key=True)
    reply_post = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='reply')
    reply_to = models.ForeignKey(Posts, on_delete=models.CASCADE, related_name='original')
    class Meta:
        ordering = ['id']