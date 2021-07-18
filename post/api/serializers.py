# 3rd-party import
from rest_framework import serializers
from drf_dynamic_fields import DynamicFieldsMixin

# Local import
from accounts.models import User
from post.models import Post, Comment


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

    
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            'user',
            'post',
            'comment',
            'reply',
        )
        extra_kwargs = {
            'user': {'read_only': True}
        }
    
    def create(self, validated_data):
        user = self.context['request'].user
        post = validated_data['post']
        comment = validated_data['comment']
        reply = validated_data['reply']
        if reply:
            Comment.objects.create(user=user, comment=comment,
             reply=reply, post=post)
        else:
            Comment.objects.create(user=user, comment=comment, post=post)
        return validated_data