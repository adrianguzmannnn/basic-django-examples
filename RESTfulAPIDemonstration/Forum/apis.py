import http
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from django.core.cache import cache
from Forum.serializers import PostSerializer, CommentSerializer
from Forum.models import Post, Comment

class PostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class PostCreate(CreateAPIView):
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    lookup_field = 'id'
    serializer_class = PostSerializer

    def delete(self, request, *args, **kwargs):
        identification = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == http.HTTPStatus.NO_CONTENT:
            cache.delete(f'post_data_{identification}')
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == http.HTTPStatus.OK:
            post = response.data
            cache.set(f'post_data_{post["id"]}', {'title': post['title'], 'body': post['body']})
        return response

class CommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id',)

class CommentCreate(CreateAPIView):
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    lookup_field = 'id'
    serializer_class = CommentSerializer

    def delete(self, request, *args, **kwargs):
        identification = request.data.get('id')
        response = super().delete(request, *args, **kwargs)
        if response.status_code == http.HTTPStatus.NO_CONTENT:
            cache.delete(f'comment_data_{identification}')
        return response

    def update(self, request, *args, **kwargs):
        response = super().update(request, *args, **kwargs)
        if response.status_code == http.HTTPStatus.OK:
            comment = response.data
            cache.set(f'comment_data_{comment["id"]}', {'body': comment['body']})
        return response