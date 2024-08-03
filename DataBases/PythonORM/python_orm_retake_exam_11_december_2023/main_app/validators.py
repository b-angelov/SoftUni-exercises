from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class RangeValueValidator(BaseValidator):

    def __init__(self, min, max, message=None):
        self.min = min
        self.max = max
        super().__init__(None, message)

    def __call__(self, value):
        if not self.min <= value <= self.max:
            raise ValidationError(self.message)

class RangeLengthValidator(BaseValidator):
    def __init__(self, min, max, message=None):
        self.min = min
        self.max = max
        super().__init__(None, message)

    def __call__(self, value):
        if not self.min <= len(value) <= self.max:
            raise ValidationError(self.message)