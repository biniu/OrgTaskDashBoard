from django.conf.urls import url, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)
router.register(r'tags', views.TagViewSet)
router.register(r'statuses', views.StatusViewSet)
router.register(r'tasks', views.TaskViewSet)

urlpatterns = [
    url(r'^api/v1/', include(router.urls)),
]
