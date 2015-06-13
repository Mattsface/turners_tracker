from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, null=False)

    def __unicode__(self):
        return self.name


class Item(models.Model):
    category = models.ForeignKey(Category)
    item_name = models.CharField(max_length=100, blank=False)
    upc_code = models.BigIntegerField(blank=True)

    def __unicode__(self):
        return self.item_name


