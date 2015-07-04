
from django.test import TestCase
from turnerwarehouse.models import Category, Item


class CategoryTestCase(TestCase):
    def test_good_category(self):
        expected = "Food"
        c1 = Category(name="Food")
        actual = unicode(c1)
        self.assertEqual(expected, actual)


class ItemTestCase(TestCase):
    fixtures = ['test_models_turners.json']
    pass
