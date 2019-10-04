from django.urls import path
from players import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('players/', views.PlayerList.as_view()),
    path('players/<int:pk>/', views.PlayerDetail.as_view()),
]
