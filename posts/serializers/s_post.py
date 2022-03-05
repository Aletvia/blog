from rest_framework import serializers
# Models
from ..models import Post

class SerializedPost(serializers.ModelSerializer):

    class Meta:
        model = Post
        exclude = ['id']