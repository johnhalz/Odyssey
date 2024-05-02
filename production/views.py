from datetime import datetime

from drf_spectacular.types import OpenApiTypes
from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import ProductionStepModel, Configuration, ProductionStep
from .serializers import ProductionStepModelSerializer, ConfigurationSerializer, ProductionStepSerializer
from Odyssey.api_common import sort, filter_by_create_ts, ModelListAPIView


@extend_schema(tags=['ProductionStepModel'])
class ProductionStepModelUpdate(generics.UpdateAPIView):
    queryset = ProductionStepModel.objects.all()
    serializer_class = ProductionStepModelSerializer
    lookup_field = 'pk'


@extend_schema(tags=['ProductionStepModel'])
class ProductionStepModelList(ModelListAPIView):

    serializer_class = ProductionStepModelSerializer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="equipment", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="step_number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="optional", required=False, type=OpenApiTypes.BOOL),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='order_by', required=False, type=str, default='id',
                         enum=['id', 'hardware_model', 'equipment', 'version', 'step_number']),
        OpenApiParameter(name='order_dir', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        super().delete(request)

    def __filter(self, request) -> list[ProductionStepModel] | Response:
        model_id = request.GET.get('id', '')
        hardware_model = request.GET.get('hardware_model', '')
        equipment = request.GET.get('equipment', '')
        version = request.GET.get('version', '')
        step_number = request.GET.get('step_number', '')
        optional = request.GET.get('optional', '')

        if model_id:
            models = [ProductionStepModel.objects.get(pk=model_id)]
        else:
            models = ProductionStepModel.objects.all()

        if hardware_model:
            models = models.filter(hardware_model=hardware_model)

        if equipment:
            models = models.filter(equipment=equipment)

        if version:
            models = models.filter(version=version)

        if step_number:
            models = models.filter(step_number=step_number)

        if optional:
            models = models.filter(optional=optional)

        models = filter_by_create_ts(request, models)
        models = sort(request, ProductionStepModel, models)

        return models

