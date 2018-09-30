from django.urls import path
from article.views import ArticleListView,ArticleDetailView

urlpatterns = [
    path('',ArticleListView.as_view(),name='articles'),
    path('<int:pk>/',ArticleDetailView.as_view(),name='article'),

]
