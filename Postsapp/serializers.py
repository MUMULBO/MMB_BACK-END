from .models import Posts, Comments
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('title', 'description','major_id','is_anony','post_point')
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comments
        fields = ('description','post_id','is_anony','token')
        