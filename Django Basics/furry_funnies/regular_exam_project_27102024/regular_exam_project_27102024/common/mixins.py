from regular_exam_project_27102024.utils.get_profile import get_profile


class CapitalizeFormFieldLabelsMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        self._capitalize_fields()


    def _capitalize_fields(self):
        for field in self.fields.values():
            field.label = ' '.join(word.capitalize() for word in field.label.split()).replace('Url','URL')

class FormFieldsDisableMixin:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._disable_fields()

    def _disable_fields(self):
        for field in self.fields.values():
            field.widget.attrs['readonly'] = 'readonly'
            # field.disabled = True

class DefaultProfileMixin:

    def get_object(self, queryset=None):
        return get_profile()