from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'players', views.PlayerViewSet)
router.register(r'paradigms', views.ParadigmViewSet)
router.register(r'programmers', views.ProgrammerViewSet)
#router.register(r'paradigms', views.ParadigmViewSet)

urlpatterns = [
  path('', include(router.urls))
]