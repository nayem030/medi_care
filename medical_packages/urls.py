from rest_framework. routers import DefaultRouter
from django.urls import path, include
from .import views
 
router = DefaultRouter() # Amader Router 

router.register('medical_package', views.MedicalPackageViewSet)
urlpatterns = [
    path('', include(router.urls)),
    
]