from django.db.models import Model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination


def sort_field(request, model) -> str | Response:
    sort_by = request.GET.get('sort_by', '')
    sort_order = request.GET.get('sort_order', 'desc')

    if not sort_by:
        sort_by = 'id'  # Set default ordering if order_by parameter is not provided

    if sort_by:
        order_field = sort_by.strip()  # Remove leading/trailing whitespaces

        # Check if the specified field exists in the model's fields
        valid_fields = [field.name for field in model._meta.get_fields()]
        if order_field not in valid_fields:
            return Response({'message': 'Invalid order_by field'}, status=status.HTTP_400_BAD_REQUEST)

        # If the field is valid, construct the sort_by clause
        if sort_order.lower() == 'desc':
            return f"-{order_field}"
        else:
            return order_field

    return '-id'


class ModelListAPIView(APIView):
    pagination_class = PageNumberPagination
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
            return Response({'message': f'{self.serializer_class.__name__} not found'}, status=status.HTTP_404_NOT_FOUND)

        for single_equipment in filtered_data:
            single_equipment.delete()

        return Response({'message': f'{self.serializer_class.__name__}(s) deleted successfully'},
                        status=status.HTTP_204_NO_CONTENT)

    def _filter(self, request):
        pass
