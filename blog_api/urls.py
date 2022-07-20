from django.urls import path

from DRF.blog_api.views import PostDetail, PostList, PostDelete

app_name = 'blog_api'

urlpatterns = (
    path('<int:pk>/', PostDetail.as_view(), name='detailcreate'),
    path('delete/<int:pk>/', PostDelete.as_view(), name='listdelete'),
    path('', PostList.as_view(), name='listcreate'),
)