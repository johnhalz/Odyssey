from datetime import datetime

from django.db.models import Q
from drf_spectacular.types import OpenApiTypes
from rest_framework import generics
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import (Measurement, SpecificationGroup, Specification, Result,
                     NonCompliance, NonComplianceComment, Processor)
from .serializers import (MeasurementSerializer, SpecificationGroupSerializer, SpecificationSerializer,
                          ResultSerializer, NonComplianceSerializer, NonComplianceCommentSerializer,
                          ProcessorSerializer)
from Odyssey.api_common import sort_field, ModelListAPIView


@extend_schema(tags=['Measurement'])
class MeasurementUpdate(generics.UpdateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Measurement'])
class MeasurementList(ModelListAPIView):

    serializer_class = MeasurementSerializer
    model = Measurement

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="production_step", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'parent', 'name', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Measurement] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'production_step':
                production_steps = value.split(',')
                production_step_filters = Q(id__in=production_steps)
                filters &= production_step_filters

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['SpecificationGroup'])
class SpecificationGroupUpdate(generics.UpdateAPIView):
    queryset = SpecificationGroup.objects.all()
    serializer_class = SpecificationGroupSerializer
    lookup_field = 'pk'


@extend_schema(tags=['SpecificationGroup'])
class SpecificationGroupList(ModelListAPIView):

    serializer_class = SpecificationGroupSerializer
    model = SpecificationGroup

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="commencement_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="commencement_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="expiration_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="expiration_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'commencement_ts', 'expiration_ts', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[SpecificationGroup] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)

            elif param == 'commencement_before':
                commencement_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(commencement_ts__lte=commencement_before_dt)
            elif param == 'commencement_after':
                commencement_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(commencement_ts__gte=commencement_after_dt)

            elif param == 'expiration_before':
                expiration_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(expiration_ts__lte=expiration_before_dt)
            elif param == 'expiration_after':
                expiration_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(expiration_ts__gte=expiration_after_dt)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Specification'])
class SpecificationUpdate(generics.UpdateAPIView):
    queryset = Specification.objects.all()
    serializer_class = SpecificationSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Specification'])
class SpecificationList(ModelListAPIView):

    serializer_class = SpecificationSerializer
    model = Specification

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="hardware_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="production_step_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="specification_group", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="severity", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'hardware_model', 'production_step_model', 'group', 'severity', 'version',
                               'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Specification] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'hardware_model':
                filters &= Q(hardware_model=value)
            elif param == 'production_step_model':
                filters &= Q(production_step_model=value)
            elif param == 'specification_group':
                filters &= Q(group=value)
            elif param == 'severity':
                filters &= Q(severity__icontains=value)
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


@extend_schema(tags=['Result'])
class ResultUpdate(generics.UpdateAPIView):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Result'])
class ResultList(ModelListAPIView):

    serializer_class = ResultSerializer
    model = Result

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="specification", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="processor", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'parent', 'specification', 'processor', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[Result] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'specification':
                filters &= Q(specification=value)
            elif param == 'processor':
                filters &= Q(processor=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['NonCompliance'])
class NonComplianceUpdate(generics.UpdateAPIView):
    queryset = NonCompliance.objects.all()
    serializer_class = NonComplianceSerializer
    lookup_field = 'pk'


@extend_schema(tags=['NonCompliance'])
class NonComplianceList(ModelListAPIView):

    serializer_class = NonComplianceSerializer
    model = NonCompliance

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="result", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="status", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="reporter", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="signer", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="closed_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="closed_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'result', 'status', 'decision', 'reporter', 'signer', 'create_ts', 'close_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[NonCompliance] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'result':
                filters &= Q(result=value)
            elif param == 'status':
                filters &= Q(status__icontains=value)
            elif param == 'reporter':
                filters &= Q(reporter=value)
            elif param == 'signer':
                filters &= Q(signer=value)

            elif param == 'closed_before':
                closed_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(close_ts__lte=closed_before_dt)
            elif param == 'closed_after':
                closed_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(close_ts__gte=closed_after_dt)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['NonComplianceComment'])
class NonComplianceCommentUpdate(generics.UpdateAPIView):
    queryset = NonComplianceComment.objects.all()
    serializer_class = NonComplianceCommentSerializer
    lookup_field = 'pk'


@extend_schema(tags=['NonComplianceComment'])
class NonComplianceCommentList(ModelListAPIView):

    serializer_class = NonComplianceCommentSerializer
    model = NonComplianceComment

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="parent", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="non_compliance", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="author", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="content", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'parent', 'non_compliance', 'author', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[NonComplianceComment] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'parent':
                filters &= Q(parent=value)
            elif param == 'non_compliance':
                filters &= Q(non_compliance=value)
            elif param == 'author':
                filters &= Q(author=value)
            elif param == 'content':
                filters &= Q(content__icontains=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)


@extend_schema(tags=['Processor'])
class ProcessorUpdate(generics.UpdateAPIView):
    queryset = Processor.objects.all()
    serializer_class = ProcessorSerializer
    lookup_field = 'pk'


@extend_schema(tags=['Processor'])
class ProcessorList(ModelListAPIView):

    serializer_class = ProcessorSerializer
    model = Processor

    open_api_params = [
        OpenApiParameter(name="id", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="name", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="version", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="production_step_model", required=False, type=OpenApiTypes.INT),
        OpenApiParameter(name="file_path", required=False, type=OpenApiTypes.STR),
        OpenApiParameter(name="created_after", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name="created_before", required=False, type=OpenApiTypes.DATETIME),
        OpenApiParameter(name='sort_by', required=False, type=str, default='id',
                         enum=['id', 'name', 'version', 'production_step_model', 'create_ts']),
        OpenApiParameter(name='sort_order', required=False, type=str, enum=['asc', 'desc'], default='desc'),
    ]

    @extend_schema(parameters=open_api_params)
    def get(self, request):
        return super().get(request)

    @extend_schema(parameters=open_api_params)
    def delete(self, request):
        return super().delete(request)

    def _filter(self, request) -> list[NonComplianceComment] | Response:
        filters = Q()

        for param, value in request.GET.items():
            if param == 'id':
                ids = value.split(',')
                id_filters = Q(id__in=ids)
                filters &= id_filters
            elif param == 'name':
                filters &= Q(name__icontains=value)
            elif param == 'version':
                filters &= Q(version=value)
            elif param == 'production_step_model':
                filters &= Q(production_step_model=value)
            elif param == 'file_path':
                filters &= Q(file_path__icontains=value)

            elif param == 'created_before':
                created_before_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__lte=created_before_dt)
            elif param == 'created_after':
                created_after_dt = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f%z")
                filters &= Q(created_ts__gte=created_after_dt)

        sort_field_str = sort_field(request, self.model_class)
        return self.model_class.objects.filter(filters).order_by(sort_field_str)
