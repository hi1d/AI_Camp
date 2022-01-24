from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('tweet/', views.tweet_show.as_view(), name='tweet'),
    path('tweet/delete/<int:id>', views.delete_tweet, name='delete_tweet'),
    path('tweet/<int:id>',views.detail_tweet,name='detail_tweet'),
    path('tweet/comment/<int:id>',views.write_comment, name='write_comment'),
    path('tweet/comment/delete/<int:id>',views.delete_comment, name='delete_comment'),
    path('tag/',views.TagCloudTV.as_view(), name='tag_cloud'),
    path('tag/<str:tag>',views.TaggedObjectLV.as_view(), name='tagged_object_list'),
]
