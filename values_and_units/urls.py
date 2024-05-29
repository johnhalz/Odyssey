from django.urls import path

from . import views

urlpatterns = [
    path("unit_type", views.UnitTypeList.as_view()),
    path("unit_type/<int:pk>", views.UnitTypeUpdate.as_view()),
    path("unit", views.UnitList.as_view()),
    path("unit/<int:pk>", views.UnitUpdate.as_view()),
    path("string", views.StringList.as_view()),
    path("string/<int:pk>", views.StringUpdate.as_view()),
    path("integer", views.IntegerList.as_view()),
    path("integer/<int:pk>", views.IntegerUpdate.as_view()),
    path("decimal", views.DecimalList.as_view()),
    path("decimal/<int:pk>", views.DecimalUpdate.as_view()),
    path("array", views.ArrayList.as_view()),
    path("array/<int:pk>", views.ArrayUpdate.as_view()),
    path("value", views.ValueList.as_view()),
    path("value/<int:pk>", views.ValueUpdate.as_view()),
    path("version", views.VersionList.as_view()),
    path("version/<int:pk>", views.VersionUpdate.as_view()),
    path("range", views.RangeList.as_view()),
    path("range/<int:pk>", views.RangeUpdate.as_view()),
]
