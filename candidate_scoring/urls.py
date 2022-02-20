from django.urls import path
from .views import candidate_list

urlpatterns = [
    path('', views.index, name='index'),
    path('create-candidate/', views.index, name='index'),
    path('create-score/', views.index, name='index'),
#     path('get-candidate/', views.index, name='index'),


]

