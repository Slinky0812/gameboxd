from django.urls import path
from . import views

urlpatterns = [
    path('', views.homeView, name='home'),
    path('create/', views.createGameView, name='gameCreate'),
    path('list/', views.readGameView, name='gameList'),
    path('update/<int:gameID>/', views.updateGameView, name='gameUpdate'),
    path('delete/<int:gameID>/', views.deleteGameView, name='gameDelete'),
]