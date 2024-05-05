from datetime import datetime

from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics, permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Hardware, HardwareModel, Order, Equipment
from .serializers import HardwareSerializer, HardwareModelSerializer, OrderSerializer, EquipmentSerializer
from Odyssey.api_common import sort_field, ModelListAPIView


@extend_schema(tags=['Hardware'])
class HardwareUpdate(generics.UpdateAPIView):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Hardware'])
class HardwareList(ModelListAPIView):

    serializer_class = HardwareSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model_class = Hardware

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="serial_number", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="set", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'serial_number', 'hardware_model', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Hardware] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id' and value:
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'serial_number' and value:
                filters &= Q(serial_number__icontains=value)
            elif param == 'set' and value:
                sets = value.split(',')
                set_filters = Q(set__in=sets)
                filters &= set_filters
            elif param == 'hardware_model' and value:
                filters &= Q(hardware_model=value)

            elif param == 'created_before' and value:
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after' and value:
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Hardware Model'])
class HardwareModelUpdate(generics.UpdateAPIView):
    queryset = HardwareModel.objects.all()
    serializer_class = HardwareModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Hardware Model'])
class HardwareModelList(ModelListAPIView):

    serializer_class = HardwareModelSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model_class = HardwareModel

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="position", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'position', 'parent', 'version', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[HardwareModel] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'position':
                filters &= Q(position__icontains=value)
            elif param == 'version':
                filters &= Q(version=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Order'])
class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Order'])
class OrderList(ModelListAPIView):

    serializer_class = OrderSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model_class = Order

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="order_type", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'number', 'hardware', 'order_type', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Order] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'number':
                order_numbers = value.split(',')
                order_number_filters = Q(number__in=order_numbers)
                filters &= order_number_filters
            elif param == 'hardware':
                filters &= Q(hardware=value)
            elif param == 'order_type':
                filters &= Q(order_type__icontains=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Equipment'])
class EquipmentUpdate(generics.UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Equipment'])
class EquipmentList(ModelListAPIView):

    serializer_class = EquipmentSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model_class = Equipment

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="status", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="calibrated_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="calibrated_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'calibration_ts', 'parent', 'status', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Equipment] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'number':
                equipment_numbers = value.split(',')
                equipment_number_filters = Q(number__in=equipment_numbers)
                filters &= equipment_number_filters
            elif param == 'status':
                filters &= Q(status__icontains=value)

            elif param == 'calibrated_before':
                calibrated_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=calibrated_before_dt)
            elif param == 'calibrated_after':
                calibrated_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=calibrated_after_dt)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)
