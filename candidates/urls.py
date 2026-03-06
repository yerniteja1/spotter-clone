from django.urls import path
from . import views

urlpatterns = [
    path('', views.candidate_list, name='candidate-list'),
    path('<int:pk>/', views.candidate_detail, name='candidate-detail'),
    path('stats/', views.stats, name='candidate-stats'),
]