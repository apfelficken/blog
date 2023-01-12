from django.urls import path
from blog.views import PostIndexView, PostView, PostAddView, PostUpdateView, PostDeleteView, CategoryPostView

app_name = 'blog'

urlpatterns = [
    path('', PostIndexView.as_view(), name='index'),
    path('<str:slug>-<int:pk>/', PostView.as_view(), name='post_detail'),
    path('post/add/', PostAddView.as_view(), name='add_post'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='update_post'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='delete_post'),
    path('category/<str:slug>/', CategoryPostView.as_view(), name='category')
]
