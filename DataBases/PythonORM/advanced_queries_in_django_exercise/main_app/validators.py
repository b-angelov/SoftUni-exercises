from decimal import Decimal

from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class InRangeValidator(BaseValidator):

    def __init__(self, min_value, max_value, message=None):
        super().__init__(None, message)
        self.min_value = min_value
        self.max_value = max_value

    def __call__(self, value):
        if not self.min_value <= value <= self.max_value:
            raise ValidationError(self.message)