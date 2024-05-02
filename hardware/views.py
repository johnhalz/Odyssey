from datetime import datetime

from drf_spectacular.types import OpenApiTypes
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import Hardware, HardwareModel, Order, Equipment
from .serializers import HardwareSerializer, HardwareModelSerializer, OrderSerializer, EquipmentSerializer
from Odyssey.api_common import sort, filter_by_create_ts


@extend_schema(tags=['Hardware'])
class HardwareUpdate(generics.UpdateAPIView):
    queryset = Hardware.objects.all()
    serializer_class = HardwareSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Hardware'])
class HardwareList(APIView):

    pagination_class = PageNumberPagination
    serializer_class = HardwareSerializer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="serial_number", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="set", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='order_by', required=False, type=str, default='id',
                         enum=['id', 'serial_number', 'hardware_model', 'create_ts']),
        OpenApiParameter(name='order_dir', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        hardware = self.__filter_hardware(request)

        if isinstance(hardware, Response):
            return hardware

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_hardware = paginator.paginate_queryset(hardware, request)

        serializer = self.serializer_class(paginated_hardware, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        try:
            hardware = self.__filter_hardware(request)
        except Hardware.DoesNotExist:
            return Response({'message': 'Hardware not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_hardware in hardware:
            single_hardware.delete()

        return Response({'message': 'Hardware deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def __filter_hardware(self, request) -> list[Hardware] | Response:
        hardware_id = request.GET.get('id', '')
        serial_number = request.GET.get('serial_number', '')
        hardware_set = request.GET.get('set', '')
        hardware_model = request.GET.get('model', '')

        if hardware_id:
            hardware = [Hardware.objects.get(pk=hardware_id)]
        else:
            hardware = Hardware.objects.all()

        if serial_number:
            hardware = hardware.filter(serial_number__icontains=serial_number)

        if hardware_set:
            hardware = hardware.filter(set=hardware_set)

        if hardware_model:
            hardware = hardware.filter(model=hardware_model)

        hardware = filter_by_create_ts(request, hardware)
        hardware = sort(request, Hardware, hardware)

        return hardware


@extend_schema(tags=['Hardware Model'])
class HardwareModelUpdate(generics.UpdateAPIView):
    queryset = HardwareModel.objects.all()
    serializer_class = HardwareModelSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Hardware Model'])
class HardwareModelList(APIView):

    pagination_class = PageNumberPagination
    serializer_class = HardwareModelSerializer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="position", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='order_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'position', 'parent', 'version', 'create_ts']),
        OpenApiParameter(name='order_dir', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        models = self.__filter_hardware_models(request)

        if isinstance(models, Response):
            return models

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_hardware = paginator.paginate_queryset(models, request)

        serializer = self.serializer_class(paginated_hardware, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        try:
            models = self.__filter_hardware_models(request)
        except HardwareModel.DoesNotExist:
            return Response({'message': 'HardwareModel not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_model in models:
            single_model.delete()

        return Response({'message': 'HardwareModel(s) deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def __filter_hardware_models(self, request) -> list[Hardware] | Response:
        hardware_model_id = request.GET.get('id', '')
        position = request.GET.get('position', '')
        version = request.GET.get('version', '')

        if hardware_model_id:
            models = [HardwareModel.objects.get(pk=hardware_model_id)]
        else:
            models = HardwareModel.objects.all()

        if position:
            models = models.filter(position__icontains=position)

        if version:
            models = models.filter(version=version)

        models = filter_by_create_ts(request, models)
        models = sort(request, HardwareModel, models)

        return models


@extend_schema(tags=['Order'])
class OrderUpdate(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Order'])
class OrderList(APIView):

    pagination_class = PageNumberPagination
    serializer_class = OrderSerializer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="hardware", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="order_type", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='order_by', required=False, type=str, default='id',
                         enum=['id', 'number', 'hardware', 'order_type', 'create_ts']),
        OpenApiParameter(name='order_dir', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        orders = self.__filter_orders(request)

        if isinstance(orders, Response):
            return orders

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_hardware = paginator.paginate_queryset(orders, request)

        serializer = self.serializer_class(paginated_hardware, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        try:
            models = self.__filter_orders(request)
        except Order.DoesNotExist:
            return Response({'message': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_model in models:
            single_model.delete()

        return Response({'message': 'Order(s) deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def __filter_orders(self, request) -> list[Hardware] | Response:
        order_id = request.GET.get('id', '')
        number = request.GET.get('number', '')
        order_type = request.GET.get('order_type', '')

        if order_id:
            orders = [Order.objects.get(pk=order_id)]
        else:
            orders = Order.objects.all()

        if number:
            orders = orders.filter(number=number)

        if order_type:
            orders = orders.filter(order_type__icontains=order_type)

        orders = filter_by_create_ts(request, orders)
        orders = sort(request, Order, orders)

        return orders


@extend_schema(tags=['Equipment'])
class EquipmentUpdate(generics.UpdateAPIView):
    queryset = Equipment.objects.all()
    serializer_class = EquipmentSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Equipment'])
class EquipmentList(APIView):

    pagination_class = PageNumberPagination
    serializer_class = EquipmentSerializer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="number", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="parent", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="status", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="calibrated_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="calibrated_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='order_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'calibration_ts', 'parent', 'status', 'create_ts']),
        OpenApiParameter(name='order_dir', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        equipment = self.__filter_equipment(request)

        if isinstance(equipment, Response):
            return equipment

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(equipment, request)

        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        try:
            equipment = self.__filter_equipment(request)
        except Equipment.DoesNotExist:
            return Response({'message': 'Equipment not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_equipment in equipment:
            single_equipment.delete()

        return Response({'message': 'Equipment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

    def __filter_equipment(self, request) -> list[Hardware] | Response:
        equipment_id = request.GET.get('id', '')
        name = request.GET.get('name', '')
        calibrated_before = request.GET.get('calibrated_before', '')
        calibrated_after = request.GET.get('calibrated_after', '')
        equipment_status = request.GET.get('status', '')

        if equipment_id:
            equipment = [Equipment.objects.get(pk=equipment_id)]
        else:
            equipment = Order.objects.all()

        if name:
            equipment = equipment.filter(name__icontains=name)

        if equipment_status:
            equipment = equipment.filter(status__icontains=equipment_status)

        if calibrated_before:
            # Attempt to format input string as a datetime
            created_before_dt = datetime.strptime(calibrated_before, "%Y-%m-%dT%H:%M:%S.%f%z")
            equipment = equipment.filter(calibration_ts__lte=created_before_dt)

        if calibrated_after:
            # Attempt to format input string as a datetime
            created_after_dt = datetime.strptime(calibrated_after, "%Y-%m-%dT%H:%M:%S.%f%z")
            equipment = equipment.filter(calibration_ts__gte=created_after_dt)

        equipment = filter_by_create_ts(request, equipment)
        equipment = sort(request, Equipment, equipment)

        return equipment
