from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class MessageHandlerMixin:

    def __init__(self, message):
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value):
        if value:
            self.__message = value
        else:
            self.__message = "An error has occurred!!"

@deconstructible
class IsAlphaValidator(MessageHandlerMixin):



    def __call__(self, value: str):
        if not value.isalpha():
            raise ValidationError(message=self.message)



@deconstructible
class ExactLengthValidator(MessageHandlerMixin):

    def __init__(self, exact_length, message=""):
        super().__init__(message)
        self.exact_length = exact_length

    def __call__(self, value: str):
        if len(value) != self.exact_length or not value.isdigit():
            raise ValidationError(self.message)
