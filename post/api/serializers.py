from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin
from accounts.models import User
from post.models import Post


# class UsernameField(serializers.RelatedField):
#     def to_representation(self, value):
#         return value.username


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username')


class PostSerializer(DynamicFieldsMixin, serializers.ModelSerializer):
    def get_username(self, obj):
        return {
            'email': obj.user.email,
            'username': obj.user.username
        }

    user = serializers.SerializerMethodField('get_username')
    # user = serializers.CharField(source='user.username', read_only=True)
    # user = serializers.HyperlinkedIdentityField(view_name='post-api:user-detail')

    class Meta:
        model = Post
        fields = (
            'id',
            'user',
            'title',
            'description',
        )
        # read_only_fields = ('user',)
    
    def validate_title(self, value):
        filter_list = ['javascript', 'php', 'laravel', 'asp.net']

        for f in filter_list:
            if f in value:
                raise serializers.ValidationError("Blog post is not about Django")