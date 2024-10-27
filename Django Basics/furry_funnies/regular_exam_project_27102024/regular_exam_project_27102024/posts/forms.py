from django import forms
from django.forms import TextInput, Textarea

from regular_exam_project_27102024.common.mixins import CapitalizeFormFieldLabelsMixin, FormFieldsDisableMixin
from regular_exam_project_27102024.posts.models import Post
from regular_exam_project_27102024.utils.get_profile import get_profile


class BasePostForm(CapitalizeFormFieldLabelsMixin, forms.ModelForm):

    def save(self, commit=True):
        form = super().save(commit=False)
        form.author_id = get_profile().pk
        form.save()

    class Meta:
        abstract = True
        fields = '__all__'
        model = Post

        labels = {
            'image_url': 'Post Image URL'
        }

        widgets = {
            'title':TextInput(
                attrs={
                    "placeholder":"Put an attractive and unique title...",
                }
            ),
            'content':Textarea(
                attrs={
                    'placeholder':"Share some interesting facts about your adorable pets...",
                }
            )
        }

class CreatePostForm(BasePostForm):
    pass

class EditPostForm(BasePostForm):

    class Meta(BasePostForm.Meta):
        help_texts = {
            'image_url':''
        }

class DeletePostForm(FormFieldsDisableMixin,EditPostForm):
    pass
