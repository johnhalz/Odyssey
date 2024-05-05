from datetime import datetime

from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics, permissions
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import UnitType, Unit, String, Integer, Decimal, Array, Value, Version, Range
from .serializers import (UnitTypeSerializer, UnitSerializer, StringSerializer, IntegerSerializer, DecimalSerializer,
                          ArraySerializer, ValueSerializer, VersionSerializer, RangeSerializer)
from Odyssey.api_common import sort_field, ModelListAPIView


@extend_schema(tags=['UnitType'])
class UnitTypeUpdate(generics.UpdateAPIView):
    queryset = UnitType.objects.all()
    serializer_class = UnitTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['UnitType'])
class UnitTypeList(ModelListAPIView):

    serializer_class = UnitTypeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = UnitType

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[UnitType] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Unit'])
class UnitUpdate(generics.UpdateAPIView):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Unit'])
class UnitList(ModelListAPIView):

    serializer_class = UnitSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Unit

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="plural_name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="type", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'type', 'abbreviation', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Unit] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'plural_name':
                filters &= Q(plural_name__icontains=value)
            elif param == 'type':
                filters &= Q(type=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['String'])
class StringUpdate(generics.UpdateAPIView):
    queryset = String.objects.all()
    serializer_class = StringSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['String'])
class StringList(ModelListAPIView):

    serializer_class = StringSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = String

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="string", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'string', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[String] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'string':
                filters &= Q(string__icontains=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Integer'])
class IntegerUpdate(generics.UpdateAPIView):
    queryset = Integer.objects.all()
    serializer_class = IntegerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Integer'])
class IntegerList(ModelListAPIView):

    serializer_class = IntegerSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Integer

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="integer", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="unit", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'integer', 'unit', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Integer] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'integer':
                filters &= Q(integer=value)
            elif param == 'unit':
                filters &= Q(unit=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Decimal'])
class DecimalUpdate(generics.UpdateAPIView):
    queryset = Decimal.objects.all()
    serializer_class = DecimalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Decimal'])
class DecimalList(ModelListAPIView):

    serializer_class = DecimalSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Decimal

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="decimal", required=False, type=OpenApiTypes.FLOAT),
        OpenApiParameter(name="unit", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'decimal', 'unit', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Decimal] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'decimal':
                filters &= Q(decimal=value)
            elif param == 'unit':
                filters &= Q(unit=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Array'])
class ArrayUpdate(generics.UpdateAPIView):
    queryset = Array.objects.all()
    serializer_class = ArraySerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Array'])
class ArrayList(ModelListAPIView):

    serializer_class = ArraySerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Array

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="unit", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'unit', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Array] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'unit':
                filters &= Q(unit=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Value'])
class ValueUpdate(generics.UpdateAPIView):
    queryset = Value.objects.all()
    serializer_class = ValueSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Value'])
class ValueList(ModelListAPIView):

    serializer_class = ValueSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Value

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Value] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Version'])
class VersionUpdate(generics.UpdateAPIView):
    queryset = Version.objects.all()
    serializer_class = VersionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Version'])
class VersionList(ModelListAPIView):

    serializer_class = VersionSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Version

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="major", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="minor", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="patch", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'major', 'minor', 'patch', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Version] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'major':
                filters &= Q(major=value)
            elif param == 'minor':
                filters &= Q(minor=value)
            elif param == 'patch':
                filters &= Q(patch=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Range'])
class RangeUpdate(generics.UpdateAPIView):
    queryset = Range.objects.all()
    serializer_class = RangeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field = 'pk'


@extend_schema(tags=['Range'])
class RangeList(ModelListAPIView):

    serializer_class = RangeSerializer
    permission_classes = (permissions.IsAuthenticated,)
    model = Range

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Range] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)
