from django.contrib import admin
from django.urls import path
from socialmediawebsite import views

urlpatterns = [
    path('', views.index, name='home' ),
    path('settings/',views.settings,name='settings'),
    path('upload/',views.upload,name='upload'),
    path('home/',views.index, name='home'),
    path('follow',views.follow, name='follow'),
    path('search/',views.search, name='search'),
    path('signup/',views.signup, name='signup'),
    path('login/',views.login, name='login'),
    path('logout/',views.logout,name='logout'),
    path('like-post',views.like_post,name='like-post'),
    path('profile/<str:pk>',views.profile, name='profile'),

]