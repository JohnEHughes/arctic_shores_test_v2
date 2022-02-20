from django.urls import path, include
from rest_framework import routers
from candidate_scoring import views
from django.contrib import admin


"""
router used to link the two new endpoints

"""



router = routers.DefaultRouter()
router.register(r'create-candidate', views.CandidateViewSet)
router.register(r'create-score', views.ScoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]

