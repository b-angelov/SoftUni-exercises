from datetime import date
from random import random

from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=500)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, null=True, blank=False)
    supplier = models.CharField(max_length=150, null=True, blank=False)
    created_on = models.DateTimeField(editable=False,auto_now_add=True)
    last_edited_on = models.DateTimeField(editable=False, auto_now=True)
    # count = models.PositiveIntegerField(default=0)
    barcode = models.IntegerField()

