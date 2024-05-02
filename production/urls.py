from django.urls import path

from . import views

urlpatterns = [
    path("production_step_model", views.ProductionStepModelList.as_view()),
    path("production_step_model/<int:pk>", views.ProductionStepModelUpdate.as_view()),
]