from django.contrib import admin
from django.urls import path,include
from Modelviewset.views import ArticleModelViewSet
from viewset.views import ArticleViewSet
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

# creating router object
router= DefaultRouter()
 
# REGISTER 
router.register('articleapi',ArticleViewSet,basename='article'),
# router.register('articleapi',ArticleModelViewSet,basename='article')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)), 
    path('gettoken/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
    ]
