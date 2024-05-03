from django.urls import path

from . import views

urlpatterns = [
    path("measurement", views.MeasurementList.as_view()),
    path("measurement/<int:pk>", views.MeasurementUpdate.as_view()),
    path("specification_group", views.SpecificationGroupList.as_view()),
    path("specification_group/<int:pk>", views.SpecificationGroupUpdate.as_view()),
    path("specification", views.SpecificationList.as_view()),
    path("specification/<int:pk>", views.SpecificationUpdate.as_view()),
    path("result", views.ResultList.as_view()),
    path("result/<int:pk>", views.ResultUpdate.as_view()),
    path("non_compliance", views.NonComplianceList.as_view()),
    path("non_compliance/<int:pk>", views.NonComplianceUpdate.as_view()),
    path("non_compliance_comment", views.NonComplianceCommentList.as_view()),
    path("non_compliance_comment/<int:pk>", views.NonComplianceCommentUpdate.as_view()),
    path("processor", views.ProcessorList.as_view()),
    path("processor/<int:pk>", views.ProcessorUpdate.as_view()),
]
