from django.urls import path

from app.views import TodoViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', TodoViewSet)
urlpatterns = router.urls

"""
urlpatterns = [
    path('', TodolistAndCreate.as_view()),
    path('<int:pk>/', TodoDetailChangeAndDelete.as_view())
]
"""





