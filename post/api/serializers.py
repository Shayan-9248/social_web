from rest_framework import serializers
from post.models import Post


class PostSerializer(serializers.ModelSerializer):
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