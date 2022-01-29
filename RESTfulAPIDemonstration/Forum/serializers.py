from rest_framework import serializers
from Forum.models import Post, Comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('pk', 'title', 'body', 'created_at', 'updated_at')

    def to_representation(self, instance):
        data = super().to_representation(instance)
        try:
            comments = instance.get_comments().values()
        except:
            return data
        else:
            data['comments'] = comments
            return data

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('pk', 'body', 'created_at', 'updated_at', 'post')
