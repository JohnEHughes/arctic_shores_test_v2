from django.urls import path
from .views import candidate_list


"""
Two url paths created for the endpoints

"""

urlpatterns = [
    path('', views.index, name='index'),
    path('create-candidate/', views.index, name='index'),
    path('create-score/', views.index, name='index'),

]

