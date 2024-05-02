from datetime import datetime

from django.db.models import F
from rest_framework import status
from rest_framework.response import Response


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
