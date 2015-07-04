
from django.test import TestCase
from turnerswarehouse.models import Category, Item


class CategoryTestCase(TestCase):
    def test_good_category(self):
        expected = "Food"
        c1 = Category(name="Food")
        actual = unicode(c1)
        self.assertEqual(expected, actual)

    def test_bad_catergry(self):
        expected = ""
        c1 = Category(name="")
        actual = unicode(c1)
        c1.save()
        self.assertEqual(expected, actual)


class ItemTestCase(TestCase):
    fixtures = ['test_models_turners.json']
    pass
