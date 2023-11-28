from django.test import TestCase
from restaurant.models import MenuItem
from decimal import Decimal


class MenuItemTest(TestCase):
    def setUp(self) -> None:
        self.item1 = MenuItem.objects.create(title="Ceaser Salad", price=9.99, inventory=5)

    def test_create_menu_item(self) -> None:
        item2 = MenuItem.objects.create(title="Pasta", price=19.00, inventory=5)
        
        self.assertEqual(MenuItem.objects.count(), 2)
        self.assertEqual(item2.title, "Pasta")
        self.assertEqual(item2.price, Decimal(19.00))
        self.assertEqual(item2.inventory, 5)

    def test_get_menu_item(self) -> None:
        item = MenuItem.objects.get(id=self.item1.id)
        
        self.assertEqual(item.title, "Ceaser Salad")
        self.assertEqual(item.price, Decimal(9.99))
        self.assertEqual(item.inventory, 5)

    def test_delete_menu_item(self) -> None:
        item = MenuItem.objects.get(id=self.item1.id)
        item.delete()
        self.assertEqual(MenuItem.objects.count(), 1)
