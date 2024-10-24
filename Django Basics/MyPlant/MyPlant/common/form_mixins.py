
class FormCapitalizingMixin:

    def form_capitalize(self, fields):
        for field in fields:
            field.label = self.__capitalize_url(self.__capitalize_words(field.label))
            field.widget.attrs['placeholder'] = self.__capitalize_url(self.__capitalize_words(field.widget.attrs.get('placeholder','')))


    def __capitalize_url(self, val: str):
        return val.replace('url', 'URL').replace('Url','URL')

    def __capitalize_words(self, val: str):
        return ' '.join(word.capitalize() for word in val.split())

class FormDisableMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.disabled = True

