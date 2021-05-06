from django.urls import path
from . import views

# Define urls within our app
urlpatterns = [
    path('', views.home, name='favourites-home'),
    path('about/', views.about, name='favourites-about'),
    path('players/', views.about, name='favourites-players'),
    path('show/', views.about, name='favourites-show'),

]