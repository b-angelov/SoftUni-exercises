from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

@deconstructible
class AlphaNumericUnderscoreValidator:

    def __init__(self, message='Username must contain only letters, digits, and underscores!'):
        self.message = message

    def __call__(self, value):
        if not value.replace("_","").isalnum():
            raise ValidationError(self.message)

@deconstructible
class ValueInRange:
    def __init__(self,lower_limit=0, upper_limit=7, message=None):
        if not message:
            message = "Year must be between %s and %s!" % (lower_limit, upper_limit,)

        self.message = message
        self.lower_limit = lower_limit
        self.upper_limit = upper_limit

    def __call__(self, value):

        if not (self.lower_limit <= value <= self.upper_limit):
            raise ValidationError(self.message)

