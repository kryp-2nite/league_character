from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(),name='home'),
    path('characters', views.Characters.as_view(),name='characters'),
    path('characters/new', views.CharacterCreate.as_view(),name='character_create'),
    path('characters/<int:pk>/', views.CharacterDetail.as_view(),name='character_detail'),
    path('characters/<int:pk>/update', views.CharacterUpdate.as_view(),name='character_update'),
    path('characters/<int:pk>/delete', views.CharacterDelete.as_view(),name='character_delete'),
    path('characters/<int:pk>/abilities/new/', views.AbilityCreate.as_view(),name='ability_create'),
    path('accounts/signup/', views.Signup.as_view(), name="signup"),
    path('accounts/profile', views.Profile.as_view(), name="profile")
]