from re import match

from django.core.exceptions import ValidationError
# from django.db import models
from django.core.validators import BaseValidator

class ValidName(BaseValidator):

    def __init__(self, *args, **kwargs):
        self.message = kwargs.get('message', "Name can only contain letters and spaces")
        super().__init__(None, **kwargs)

    def __call__(self, value):
        if not isinstance(value, str) or not value.replace(' ','').isalpha():
            raise ValidationError(self.message)


class CountryPhoneNumberValidator(BaseValidator):

    def __init__(self, *args, **kwargs):
        self.phone_code = kwargs.get('country_code','+359')
        try:
            del kwargs['country_code']
        except:
            pass
        self.message = kwargs.get('message',f"Phone number must start with '{self.phone_code}' followed by 9 digits")
        super().__init__(None,**kwargs)

    def __call__(self, value):
        pattern = fr'^\{self.phone_code}\d{{9}}$'
        if not match(pattern, value):
            raise ValidationError(self.message)
