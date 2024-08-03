from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class DigitValidator(BaseValidator):

    def __call__(self, value: str):
        if not value.isdigit():
            raise ValidationError(self.message)