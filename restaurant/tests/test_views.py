from django.test import TestCase
from restaurant.models import MenuItem


class MenuViewTest(TestCase):
    def setUp(self):
        MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        MenuItem.objects.create(title="IceCream2", price=90, inventory=100)
        MenuItem.objects.create(title="IceCream3", price=100, inventory=100)

    def test_getall(self):
        items = MenuItem.objects.all()
        for item in items:
            self.assertEqual(item.inventory, 100)
