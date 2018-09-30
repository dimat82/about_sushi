from django.urls import path
from menu.views import RollsList,SetList,SushisList,SoupList,RollDetail,SetDetail,SoupDetail,SushiDetail,Menu

urlpatterns = [
    path('',Menu.as_view(),name='menu'),
    path('rolls/',RollsList.as_view(),name='rolls'),
    path('sets/',SetList.as_view(),name='sets'),
    path('sushi/',SushisList.as_view(),name='sushi'),
    path('soups/',SoupList.as_view(),name='soups'),
    path('rolls/<int:pk>/',RollDetail.as_view(),name='roll_detail'),
    path('sets/<int:pk>/',SetDetail.as_view(),name='set_detail'),
    path('sushi/<int:pk>/',SushiDetail.as_view(),name='sushi_detail'),
    path('soups/<int:pk>',SoupDetail.as_view(),name='soup_detail'),

]
