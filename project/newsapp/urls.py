from django.urls import path
from .views import *


urlpatterns = [
   path('', NewsList.as_view(), name='news_list'),
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('search/', PostSearch.as_view(), name='post_search'),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
   # path('arcticle/create/', ArticleCreate.as_view(), name='article_create'),
   # path('article/<int:pk>/edit/', ArticleUpdate.as_view(), name='article_edit'),
   # path('article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
]
