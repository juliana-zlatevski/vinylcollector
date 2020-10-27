from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='vinyls_index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_info, name='info'),
    path('vinyls/<int:vinyl_id>/add_review', views.add_review, name='add_review')
]