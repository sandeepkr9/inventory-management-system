from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from .models import Item

class ItemTests(APITestCase):

    def test_create_item(self):
        url = reverse('create-item')
        data = {'name': 'Test Item', 'description': 'Test Description', 'quantity': 10}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_read_item(self):
        item = Item.objects.create(name='Test Item', description='Test Description', quantity=10)
        url = reverse('read-item', args=[item.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
