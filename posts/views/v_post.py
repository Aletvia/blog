from django.core.handlers.wsgi import WSGIRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
#Models
from ..models import Post
#Serializers
from posts.serializers.s_post import SerializedPost

class PostApiView(APIView):
    """
        View dedicated to:
            - List all existing all the questions by service
            - Retrieve an existing relation between a service and a question
    """
    def get( self, request: WSGIRequest, uuid4=None ):
        try:
            if uuid4:
                query_data = Post.objects.filter(uuid4=uuid4)
            else:
                query_data = Post.objects.order_by('created_at','id')
            serialized_data = SerializedPost( query_data, many = True )
            return Response( 
                            {'status': 'ok', 'data': serialized_data.data}, 
                            status=status.HTTP_200_OK)
        except Post.DoesNotExist:
            return Response(
                {'status': 'bad', 'error': 'Post not found'},
                status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(
                {'status': 'bad', 'error': "Exception In Index: " + str(e)}, 
                status=status.HTTP_400_BAD_REQUEST)