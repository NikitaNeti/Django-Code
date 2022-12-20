from django.urls import path
from . import views
# from rest_framework.authtoken import views
urlpatterns = [
    # path('list/',views.article_list),
    # path('details/<int:pk>/', views.article_detail),

    # path('listclass/',views.ArticleList.as_view()),
    # path('detailclass/<int:pk>/',views.ArticleDetail.as_view()),

    path('generic/list/',views.GenericAPIView.as_view()),
    path('generic/detail/<int:id>/',views.DetailGenericAPI.as_view()),

    # path('list/generic/',views.Genericlist.as_view()),
    # path('details/generic/<int:id>/',views.GenericDetail.as_view()),

    # path('gettoken/', views.obtain_auth_token)
]