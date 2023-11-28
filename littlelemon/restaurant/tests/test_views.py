from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status

from restaurant.models import MenuItem
from restaurant.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        self.user = User.objects.create_user(
            username="admin", password="admin"
        )

        self.pasta = MenuItem.objects.create(title="pasta", price=14.99, inventory=20)
        self.salad = MenuItem.objects.create(title="salad", price=5.99, inventory=10)

    def test_getall(self):
        self.client.login(username="admin", password="admin")
        response = self.client.get(reverse("menu"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        menu = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu, many=True)
        self.assertEqual(response.data, serializer.data)
