from typing import Any

from django.db.models import Model
from drf_spectacular.utils import OpenApiParameter, OpenApiResponse
from rest_framework import serializers, status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView


def sort_field(request, model) -> str | Response:
    sort_by = request.GET.get("sort_by", "")
    sort_order = request.GET.get("sort_order", "desc")

    if not sort_by:
        sort_by = "id"  # Set default ordering if order_by parameter is not provided

    if sort_by:
        order_field = sort_by.strip()  # Remove leading/trailing whitespaces

        # Check if the specified field exists in the model's fields
        valid_fields = [field.name for field in model._meta.get_fields()]
        if order_field not in valid_fields:
            return Response(
                {"message": "Invalid order_by field"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # If the field is valid, construct the sort_by clause
        if sort_order.lower() == "desc":
            return f"-{order_field}"
        else:
            return order_field

    return "-id"


class PaginatedSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    next = serializers.CharField(allow_null=True)
    previous = serializers.CharField(allow_null=True)
    results = serializers.ListField()

    def __init__(self, *args, **kwargs):
        child_serializer = kwargs.pop("child", None)
        super().__init__(*args, **kwargs)
        if child_serializer is not None:
            self.fields["results"] = serializers.ListSerializer(
                child=child_serializer()
            )

    @classmethod
    def create_paginated_serializer(cls, child_serializer):
        def __init__(self, *args, **kwargs):
            super(self.__class__, self).__init__(
                *args, **kwargs, child=child_serializer
            )

        # Creating the new class dynamically with the specified name
        CustomPaginatedSerializer = type(
            f"{child_serializer.__name__}PaginatedSerializer",
            (cls,),
            {"__init__": __init__},
        )

        return CustomPaginatedSerializer


class PaginationView(PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 500


class ModelListAPIView(APIView):
    pagination_class = PaginationView
    serializer_class = None
    model_class: Model = None
    open_api_params = []

    def get(self, request, *args, **kwargs):
        filtered_data = self._filter(request)

        if isinstance(filtered_data, Response):
            return filtered_data

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_queryset = paginator.paginate_queryset(filtered_data, request)

        serializer = self.serializer_class(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            filtered_data = self._filter(request)
        except self.model_class.DoesNotExist:
            return Response(
                {"message": f"{self.serializer_class.__name__} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        for single_equipment in filtered_data:
            single_equipment.delete()

        return Response(
            {"message": f"{self.serializer_class.__name__}(s) deleted successfully"},
            status=status.HTTP_204_NO_CONTENT,
        )

    def _filter(self, request):
        pass

    def __pagniate_api_params(self) -> list[OpenApiParameter]:
        return []
