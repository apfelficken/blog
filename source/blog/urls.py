from django.urls import path
from blog.views import PostIndexView, PostView, PostAddView, PostUpdateView, PostDeleteView, CategoryPostView, \
    PostCommentCreateView, CommentUpdateView, CommentDeleteView

app_name = 'blog'

urlpatterns = [
    path('', PostIndexView.as_view(), name='index'),
    path('<str:slug>-<int:pk>/', PostView.as_view(), name='post_detail'),
    path('post/add/', PostAddView.as_view(), name='add_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('category/<str:slug>/', CategoryPostView.as_view(), name='category'),
    path('post/<int:pk>/comment/add/', PostCommentCreateView.as_view(), name='post_comment_add'),
    path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment_update'),
    path('comment/<int:pk>/delete/', CommentDeleteView.as_view(), name='comment_delete'),
]
