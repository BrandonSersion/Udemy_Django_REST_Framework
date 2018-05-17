from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import HelloApiView, HelloViewset, UserProfileViewSet

router = DefaultRouter()
router.register('hello-viewset', HelloViewset, base_name='hello-viewset')
router.register('profile', UserProfileViewSet)

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls)),
]
