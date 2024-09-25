from rest_framework.serializers import ModelSerializer

from .models import Movie, Category, Comment

class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
