from django.urls import include, path
from rest_framework import routers

from .views import HospitalView, ProcedureView


router = routers.DefaultRouter()
router.register('hospital',HospitalView)
router.register('procedure',ProcedureView)

urlpatterns = [
    path('',include(router.urls))
]
