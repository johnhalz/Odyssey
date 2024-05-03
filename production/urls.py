from django.urls import path

from . import views

urlpatterns = [
    path("production_step_model", views.ProductionStepModelList.as_view()),
    path("production_step_model/<int:pk>", views.ProductionStepModelUpdate.as_view()),
    path("configuration", views.ConfigurationList.as_view()),
    path("configuration/<int:pk>", views.ConfigurationUpdate.as_view()),
    path("production_step", views.ProductionStepList.as_view()),
    path("production_step/<int:pk>", views.ProductionStepUpdate.as_view()),
]
