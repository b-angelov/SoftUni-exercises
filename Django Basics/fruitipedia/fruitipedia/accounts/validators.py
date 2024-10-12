from django.utils.deconstruct import deconstructible
from prompt_toolkit.validation import ValidationError


@deconstructible
class BaseModelValidator:
    validation_function = lambda *args, **kwargs: None
    error_message = ''

    def __init__(self, error_message = None, validation_function = None):
        if error_message:
            self.error_message= error_message
        if validation_function:
            self.validation_function = validation_function

    def __call__(self, value, validation_function=None, *args, **kwargs):
        function = validation_function or self.validation_function
        if not function(value):
            raise ValidationError(message=self.error_message)


@deconstructible
class FirstAlphaValidator(BaseModelValidator):
    validation_function = lambda obj,value: value[0].isalpha


@deconstructible
class IsAlphaValidator(BaseModelValidator):
    validation_function = lambda obj,value: value.isalpha
