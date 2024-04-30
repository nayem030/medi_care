from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('list', views.DoctorViewset)
router.register('department', views.DepartmentViewset)
router.register('specialization', views.SpecializationViewset)
router.register('designation', views.DesignationViewset)
router.register('reviews', views.ReviewViewset)


urlpatterns = [
    path('', include(router.urls)),
]