from django.urls import path, include
from rest_framework.routers import DefaultRouter
from restapi.views import TaskViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('task', TaskViewSet, 'task')

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.obtain_auth_token),
]