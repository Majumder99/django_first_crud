from django.urls import path
from . import views

urlpatterns = [
    path('view', views.add_show, name="add_show"),
    path('delete/<int:id>', views.delete_data, name="delete_data"),
    path('edit/<int:id>', views.edit_data, name="edit_data"),
]
