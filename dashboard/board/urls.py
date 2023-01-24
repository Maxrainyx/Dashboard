from django.urls import path
from .views import (
   PostList, PostDetail, PostCreate, PostUpdate, PostDelete, UserView, CommentCreate, comment_approve, comment_delete
)
from django.views.decorators.cache import cache_page

urlpatterns = [
   path('', PostList.as_view(), name='post_list'),
   path('<int:pk>', (PostDetail.as_view()), name='post_detail'),
   path('<int:pk>/update/', PostUpdate.as_view(), name='post_update'),
   path('create/', PostCreate.as_view(), name='post_create'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
   path('<int:pk>/comment/', CommentCreate.as_view(), name='comment_create'),

   path('profile/', UserView.as_view(), name='profile'),
   path('approve/<int:pk>', comment_approve, name='comment_approve'),

   path('delete/<int:pk>', comment_delete, name='comment_delete'),

   path('', UserView.as_view(), name='user'),

]