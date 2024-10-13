from django import forms

from my_music_app.accounts.models import Profile
from my_music_app.album.models import Album


class AlbumBaseForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        disable = ''
        if 'disable' in kwargs:
            disable = kwargs.pop('disable')
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.label = field.label.capitalize()
            if 'url' in field.label.lower():
                field.label = 'Image URL'
            if name in disable or disable == '__all__':
                field.disabled = True
            field.widget.attrs['placeholder'] = field.label


    class Meta:
        model=Album
        fields = '__all__'
        abstract = True

    def save(self, commit=True):
        obj = super().save(commit=False)
        obj.owner_id = Profile.get_last_profile().pk
        obj.save()

class CreateAlbumForm(AlbumBaseForm):
    pass

class EditAlbumForm(AlbumBaseForm):
    pass

class DeleteAlbumForm(AlbumBaseForm):

    def __init__(self, *args, **kwargs):
        kwargs['disable'] = '__all__'
        super().__init__(*args, **kwargs)



