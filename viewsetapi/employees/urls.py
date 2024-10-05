from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from django.urls import path, include

router = DefaultRouter()
router.register('employee', EmployeeViewSet) 

urlpatterns = [
    path('api/', include(router.urls)),
]
