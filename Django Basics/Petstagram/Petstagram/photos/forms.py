from django import forms
from Petstagram.photos.models import Photo


class PhotoCreateForm(forms.ModelForm):

    class Meta:
        model = Photo
        fields = "__all__"


class PhotoEditForm(forms.ModelForm):

    class Meta:
        model = Photo
        exclude = ["photo"]