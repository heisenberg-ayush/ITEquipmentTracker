from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_equipment/', views.add_equipment, name='add_equipment'),
    path('delete_equipment/', views.delete_equipment, name='delete_equipment'),
    path('edit_equipment/', views.edit_equipment, name='edit_equipment'),
]
