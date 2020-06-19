from rest_framework import serializers

from posts.models import Post, Comment


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        fields = "__all__"
        model = Comment
        read_only_fields = ["post"]


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    # comments = CommentSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = Post
