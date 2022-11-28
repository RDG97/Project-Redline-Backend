from rest_framework import serializers
from redline.models import CustomUser

class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    filter_explicit = serializers.BooleanField(required=True)
    screen_name = serializers.CharField(required=True, allow_blank=False)
    bio = serializers.CharField(required=True, allow_blank=False)
    profile_pic = serializers.URLField()
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
