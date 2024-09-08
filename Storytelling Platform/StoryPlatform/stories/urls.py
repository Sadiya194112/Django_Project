from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.create_story, name='create_story'),
    path('add_chapter/<int:pk>/', views.add_chapter, name='add_chapter'),
    path('read/<int:pk>/', views.read_story, name='read_story'),  # Read story entry point
    path('read/<int:pk>/<int:chapter_id>/', views.read_story, name='read_chapter'),  # Read specific chapter
    path('', views.dashboard, name='dashboard'),


    #Login and Logout
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.custom_logout_view, name='logout'),
]
