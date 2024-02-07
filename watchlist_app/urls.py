from django.contrib import admin
from django.urls import path,include
from .views import movie_list,movie_description 



urlpatterns = [
    path('admin/', admin.site.urls),
    path( 'list/',movie_list,name='movie-list'),
    path('<int:pk>',movie_description,name='movie-description')]




