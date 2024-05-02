from datetime import datetime

from django.db.models import F, Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


def sort(request, model, existing_list):
    order_by = request.GET.get('order_by', '')
    order_dir = request.GET.get('order_dir', 'desc')

    if not order_by:
        order_by = 'id'  # Set default ordering if order_by parameter is not provided

    if order_by:
        order_field = order_by.strip()  # Remove leading/trailing whitespaces

        # Check if the specified field exists in the model's fields
        valid_fields = [field.name for field in model._meta.get_fields()]
        if order_field not in valid_fields:
            return Response({'message': 'Invalid order_by field'}, status=status.HTTP_400_BAD_REQUEST)

        # If the field is valid, construct the order_by clause
        if order_dir.lower() == 'desc':
            order_field = F(order_field).desc()
        else:
            order_field = F(order_field).asc()

        return existing_list.order_by(order_field)


def filter_by_create_ts(request, existing_list):
    created_before = request.GET.get('created_before', '')
    created_after = request.GET.get('created_after', '')

    if created_before:
        # Attempt to format input string as a datetime
        created_before_dt = datetime.strptime(created_before, "%Y-%m-%dT%H:%M:%S.%f%z")
        existing_list = existing_list.filter(create_ts__lte=created_before_dt)

    if created_after:
        # Attempt to format input string as a datetime
        created_after_dt = datetime.strptime(created_after, "%Y-%m-%dT%H:%M:%S.%f%z")
        existing_list = existing_list.filter(create_ts__gte=created_after_dt)

    return existing_list


def filter_by_update_ts(request, existing_list):
    updated_before = request.GET.get('updated_before', '')
    updated_after = request.GET.get('updated_after', '')

    if updated_before:
        # Attempt to format input string as a datetime
        updated_before_dt = datetime.strptime(updated_before, "%Y-%m-%dT%H:%M:%S.%f%z")
        existing_list = existing_list.filter(update_ts__lte=updated_before_dt)

    if updated_after:
        # Attempt to format input string as a datetime
        updated_after_dt = datetime.strptime(updated_after, "%Y-%m-%dT%H:%M:%S.%f%z")
        existing_list = existing_list.filter(update_ts__gte=updated_after_dt)

    return existing_list


class ModelListAPIView(APIView):
    pagination_class = PageNumberPagination
    serializer_class = None
    model_class: Model = None
    open_api_params = []

    def get(self, request, *args, **kwargs):
        filtered_data = self.__filter(request)

        if isinstance(filtered_data, Response):
            return filtered_data

        # Paginate the queryset
        paginator = self.pagination_class()
        paginated_data = paginator.paginate_queryset(filtered_data, request)

        serializer = self.serializer_class(paginated_data, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        try:
            filtered_data = self.__filter(request)
        except self.model_class.DoesNotExist:
            return Response({'message': f'{self.serializer_class.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_equipment in filtered_data:
            single_equipment.delete()

        return Response({'message': f'{self.serializer_class.__name__}(s) deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)

    def __filter(self, request) -> list[Model] | Response:
        pass
