from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class ValidateImageSize(BaseValidator):

    def __init__(self, allowed_size=5242880, message="Image exceeds file size limit!"):
        super().__init__(allowed_size, message)

    def __call__(self, value):
        value = value.size
        super().__call__(value)

    def compare(self, a,b):
        return a > b

