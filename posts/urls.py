from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('post/', views.create_post, name='post'),
    path('comment/<int:post_id>', views.create_comment, name='comment')
]
