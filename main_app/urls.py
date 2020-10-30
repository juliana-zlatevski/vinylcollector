from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('vinyls/', views.vinyls_index, name='vinyls_index'),
    path('vinyls/<int:vinyl_id>/', views.vinyls_info, name='info'),
    path('vinyls/<int:vinyl_id>/add_review', views.add_review, name='add_review'),
    path('vinyls/<int:vinyl_id>/assoc_mood/<int:mood_id>/', views.assoc_mood, name='assoc_mood'),
    path('vinyls/<int:vinyl_id>/remove_mood/<int:mood_id>/', views.remove_mood, name='remove_mood'),
    path('vinyls/<int:vinyl_id>/delete_vinyl/', views.delete_vinyl, name='delete_vinyl'),
    path('vinyls/<int:vinyl_id>/edit_vinyl/', views.edit_vinyl, name='edit_vinyl'),
    path('vinyls/add_vinyl', views.add_vinyl, name='add_vinyl')
]