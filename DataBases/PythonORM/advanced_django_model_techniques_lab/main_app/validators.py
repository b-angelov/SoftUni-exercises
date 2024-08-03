import django.core.validators
from django.core.exceptions import ValidationError
from django.core.validators import BaseValidator


class validate_menu_categories(BaseValidator):

    def __init__(self, *args, **kwargs):
        kwargs['limit_value'] = kwargs.get('limit_value', ["Appetizers", "Main Course","Desserts"])
        kwargs['message'] = kwargs.get('message','The menu must include each of the categories "Appetizers", "Main Course", "Desserts".')
        self.includes = kwargs['limit_value']
        self.message = kwargs['message']
        super().__init__(*args,**kwargs)

    def __call__(self, value):
        for dish in self.includes:
            if dish not in value:
                raise ValidationError(self.message)