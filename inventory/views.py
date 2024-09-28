from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from django.core.cache import cache
from .models import Item
from .serializers import ItemSerializer
import logging

logger = logging.getLogger(__name__)

class CreateItemView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReadItemView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        cache_key = f'item_{item_id}'
        item = cache.get(cache_key)

        if not item:
            item = get_object_or_404(Item, id=item_id)
            cache.set(cache_key, item, timeout=60*15)  # Cache for 15 minutes

        serializer = ItemSerializer(item)
        return Response(serializer.data)


class UpdateItemView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        serializer = ItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            cache.delete(f'item_{item_id}')  # Invalidate cache
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteItemView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, item_id):
        item = get_object_or_404(Item, id=item_id)
        item.delete()
        cache.delete(f'item_{item_id}')  # Invalidate cache
        return Response({"message": "Item deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
