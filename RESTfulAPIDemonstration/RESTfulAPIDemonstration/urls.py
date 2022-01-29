import Forum.views
import Forum.apis
from django.contrib import admin
from django.urls import path


urlpatterns = [
    # Handle the post CRUD operations.
    path('api/v1/posts/', Forum.apis.PostList.as_view()),
    path('api/v1/posts/new', Forum.apis.PostCreate.as_view()),
    path('api/v1/posts/<int:id>', Forum.apis.PostRetrieveUpdateDestroy.as_view()),

    # Handle the comment CRUD operations.
    path('api/v1/comments/', Forum.apis.CommentList.as_view()),
    path('api/v1/comments/new', Forum.apis.CommentCreate.as_view()),
    path('api/v1/comments/<int:id>', Forum.apis.CommentRetrieveUpdateDestroy.as_view()),

    # Handle admin routes.
    path('admin/', admin.site.urls),
]
