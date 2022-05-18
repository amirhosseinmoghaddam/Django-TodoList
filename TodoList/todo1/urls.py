from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('delete/<int:list_id>', views.delete, name="delete"),
    path('item/complete/<int:list_id>', views.complete, name="complete"),
    path('item/completed/<int:list_id>', views.completed, name="completed"),
    path('item/edit/<int:list_id>', views.edit, name="edit"),
]