from django.urls import path

from . import views


urlpatterns = [
    path("hardware", views.HardwareList.as_view()),
    path("hardware/<int:pk>", views.HardwareUpdate.as_view()),
    path("hardware_model", views.HardwareModelList.as_view()),
    path("hardware_model/<int:pk>", views.HardwareModelUpdate.as_view()),
    path("order", views.OrderList.as_view()),
    path("order/<int:pk>", views.OrderUpdate.as_view()),
    path("equipment", views.EquipmentList.as_view()),
    path("equipment/<int:pk>", views.EquipmentUpdate.as_view())
]
