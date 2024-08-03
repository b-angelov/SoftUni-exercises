from django.db import models
from django.db.models import Count


class ProfileManager(models.Manager):

    def get_regular_customers(self):
        return self.annotate(order_count=Count("order")).filter(order_count__gt=2).order_by('-order_count')