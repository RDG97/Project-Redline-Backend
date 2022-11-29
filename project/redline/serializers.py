from rest_framework import serializers
from redline.models import CustomUser, Is_following, Posts, Post_reply, Post_likes

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    filter_explicit = serializers.BooleanField(required=True)
    screen_name = serializers.CharField(required=True, allow_blank=False)
    bio = serializers.CharField(required=True, allow_blank=False)
    profile_pic = serializers.URLField(allow_blank=True)
    bgImage = serializers.URLField(required=False)
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)
    class Meta:
        model = CustomUser
        fields = ['filter_explicit', 'screen_name', 'bio', 'profile_pic', 'bgImage', 'username', 'password', 'email',]
    def create(self, validated_data):
        return CustomUser.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.filter_explicit = validated_data.get('filter_explicit', instance.filter_explicit)
        instance.screen_name = validated_data.get('screen_name', instance.screen_name)
        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_pic = validated_data.get('profile_pic', instance.profile_pic)
        instance.bgImage = validated_data.get('bgImage', instance.bgImage)
        instance.username = validated_data.get('username', instance.username)
        instance.password = validated_data.get('password', instance.password)
        instance.email = validated_data.get('email', instance.email)
        instance.save()
        return instance

class IsFollowingSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    follower = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=CustomUser.objects.all()
    )
    followed = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=CustomUser.objects.all()
    )
    class Meta:
        model = Is_following
        fields = ['follower', 'followed',]
    def create(self, validated_data):
        return Is_following.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.follower = validated_data.get('follower', instance.follower)
        instance.followed = validated_data.get('followed', instance.followed)
        instance.save()
        return instance

class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=CustomUser.objects.all()
    )
    text_content = serializers.CharField(required=True, allow_blank=False)
    media_link = serializers.URLField(required=False)
    explicit = serializers.BooleanField(required=True)
    class Meta:
        model = Posts
        fields = ['author', 'text_content', 'media_link', 'explicit',]
    def create(self, validated_data):
        return Posts.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instace.author)
        instance.text_content = validated_data.get('text_content', instance.text_content)
        instance.media_link = validated_data.get('media_link', instance.media_link)
        instance.explicit = validated_data.get('explicit', instance.explicit)
        instance.save()
        return instance

class PostReplySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    reply_post = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Posts.objects.all()
    )
    reply_to = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Posts.objects.all()
    )
    class Meta:
        model = Post_reply
        fields = ['reply_post', 'reply_to',]
    def create(self, validated_data):
        return Post_reply.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.reply_post = validated_data.get('reply_post', instance.reply_post)
        instance.reply_to = validated_data.get('reply_to', instance.reply_to)
        instance.save()
        return instance

class PostLikesSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    liker = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=CustomUser.objects.all()
    )
    post = serializers.PrimaryKeyRelatedField(
    many=False,
    queryset=Posts.objects.all()
    )
    class Meta:
        model = Post_likes
        fields = ['liker', 'post',]
    def create(self, validated_data):
        return Post_likes.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.liker = validated_data.get('liker', instance.liker)
        instance.post = validated_data.get('post', instance.post)
        instance.save()
        return instance