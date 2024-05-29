from datetime import datetime

from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, permissions
from rest_framework.response import Response

from Odyssey.api_common import ModelListAPIView, PaginatedSerializer, sort_field

from .models import Configuration, ProductionStep, ProductionStepModel
from .serializers import (
    ConfigurationSerializer,
    ProductionStepModelSerializer,
    ProductionStepSerializer,
)


@extend_schema(tags=["ProductionStepModel"])
class ProductionStepModelUpdate(generics.UpdateAPIView):
    queryset = ProductionStepModel.objects.all()
    serializer_class = ProductionStepModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


@extend_schema(tags=["ProductionStepModel"])
class ProductionStepModelList(ModelListAPIView):

    serializer_class = ProductionStepModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = ProductionStepModel

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="equipment", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="step_number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="optional", required=False, type=OpenApiTypes.BOOL),
        OpenApiParameter(
            name="created_after", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="created_before", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="sort_by",
            required=False,
            type=str,
            default="id",
            enum=["id", "hardware_model", "equipment", "version", "step_number"],
        ),
        OpenApiParameter(
            name="sort_order",
            required=False,
            type=str,
            enum=["asc", "desc"],
            default="desc",
        ),
    ]

    @extend_schema(
        parameters=open_api_params,
        responses={
            200: PaginatedSerializer.create_paginated_serializer(
                ProductionStepModelSerializer
            )
        },
    )
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[ProductionStepModel] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == "id":
                ids = value.split(",")
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == "hardware_model":
                filters &= Q(hardware_model=value)
            elif param == "equipment":
                filters &= Q(equipment=value)
            elif param == "version":
                filters &= Q(version=value)
            elif param == "step_number":
                filters &= Q(step_number=value)
            elif param == "optional":
                filters &= Q(optional=value)

            elif param == "created_before":
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == "created_after":
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=["Configuration"])
class ConfigurationUpdate(generics.UpdateAPIView):
    queryset = Configuration.objects.all()
    serializer_class = ConfigurationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


@extend_schema(tags=["Configuration"])
class ConfigurationList(ModelListAPIView):

    serializer_class = ConfigurationSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Configuration

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(
            name="production_step_model", required=False, type=OpenApiTypes.INT
        ),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(
            name="created_after", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="created_before", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="sort_by",
            required=False,
            type=str,
            default="id",
            enum=[
                "id",
                "name",
                "value",
                "hardware_model",
                "production_step_model",
                "version",
                "create_ts",
            ],
        ),
        OpenApiParameter(
            name="sort_order",
            required=False,
            type=str,
            enum=["asc", "desc"],
            default="desc",
        ),
    ]

    @extend_schema(
        parameters=open_api_params,
        responses={
            200: PaginatedSerializer.create_paginated_serializer(
                ConfigurationSerializer
            )
        },
    )
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Configuration] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == "id":
                ids = value.split(",")
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == "name":
                filters &= Q(name__icontaints=value)
            elif param == "hardware_model":
                filters &= Q(hardware_model=value)
            elif param == "production_step_model":
                filters &= Q(production_step_model=value)
            elif param == "version":
                filters &= Q(version=value)

            elif param == "created_before":
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == "created_after":
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=["ProductionStep"])
class ProductionStepUpdate(generics.UpdateAPIView):
    queryset = ProductionStep.objects.all()
    serializer_class = ProductionStepSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = "pk"


@extend_schema(tags=["ProductionStep"])
class ProductionStepList(ModelListAPIView):

    serializer_class = ProductionStepSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model_class = ProductionStep

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="order", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(
            name="production_step_model", required=False, type=OpenApiTypes.INT
        ),
        OpenApiParameter(name="status", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="operator", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(
            name="started_after", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="started_before", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="ended_after", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="ended_before", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="created_after", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="created_before", required=False, type=OpenApiTypes.DATETIME
        ),
        OpenApiParameter(
            name="sort_by",
            required=False,
            type=str,
            default="id",
            enum=[
                "id",
                "order",
                "production_step_model",
                "status",
                "operator",
                "start_ts",
                "end_ts",
                "create_ts",
            ],
        ),
        OpenApiParameter(
            name="sort_order",
            required=False,
            type=str,
            enum=["asc", "desc"],
            default="desc",
        ),
    ]

    @extend_schema(
        parameters=open_api_params,
        responses={
            200: PaginatedSerializer.create_paginated_serializer(
                ProductionStepSerializer
            )
        },
    )
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[ProductionStep] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == "id":
                ids = value.split(",")
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == "order":
                filters &= Q(order=value)
            elif param == "production_step_model":
                filters &= Q(production_step_model=value)
            elif param == "status":
                filters &= Q(status__icontains=value)
            elif param == "operator":
                filters &= Q(operator=value)

            elif param == "started_before":
                started_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(start_ts__lte=started_before_dt)
            elif param == "started_after":
                started_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(start_ts__gte=started_after_dt)
            elif param == "ended_before":
                ended_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(end_ts__lte=ended_before_dt)
            elif param == "ended_after":
                ended_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(end_ts__gte=ended_after_dt)

            elif param == "created_before":
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == "created_after":
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)
