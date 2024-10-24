from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible

class MessageMixin:
    DEFAULT_MESSAGE = 'An error has occurred!'

    def __init__(self, message=None):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value:
            self.__message = value
        else:
            self.message = self.DEFAULT_MESSAGE

@deconstructible
class FirstCapitalValidator(MessageMixin):

    def __call__(self, value: str):
        if not value[0].isupper():
            raise ValidationError(self.message)



@deconstructible
class IsAlphaValidator(MessageMixin):

    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(self.message)



