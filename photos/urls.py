from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_view, name='gallery'),
    path('photo/<int:pk>/', views.photo_details_view, name='photo'),
    path('add/', views.add_photo_view, name='add'),

    # path('<int:pk>/', views.photo_details_view, name='photo'),
]
  