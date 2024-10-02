from django.utils.deconstruct import deconstructible
from prompt_toolkit.validation import ValidationError


@deconstructible
class FirstCapital:

    def __init__(self, message="Name must start with a capital letter!"):
        self.message = message

    def __call__(self, value, message=None):
        if not value or not value[0].isupper():
            raise ValidationError(message or self.message)

