from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='cars_index'),
    path('cars/<int:car_id>/', views.cars_detail, name='cars_detail'),
    path('cars/create/', views.CarCreate.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='car_delete'),

    path('mods/', views.mods_index, name='mods_index'),
    path('mods/<int:mod_id>/', views.mods_detail, name='mods_detail'),
    path('mods/create/', views.ModCreate.as_view(), name='mods_create'),
    path('mods/<int:pk>/update/', views.ModUpdate.as_view(), name='mod_update'),
    path('mods/<int:pk>/delete/', views.ModDelete.as_view(), name='mod_delete'),
    path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),

    path('cars/<int:car_id>/assoc_mod/<int:mod_id>/', views.assoc_mod, name='assoc_mod'),
    path('cars/<int:car_id>/unassoc_mod/<int:mod_id>/', views.unassoc_mod, name='unassoc_mod'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo')
]