from django.apps import apps
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy


# Create your views here.

def index(request):

    Photo = apps.get_model('photos', 'Photo')
    photos = Photo.get_all_photos()
    details_url = request.get_full_path()

    context = {
        'photos': photos,
        'url': details_url,
    }

    return render(request, 'common/home-page.html', context)


def like_functionality(request, photo_id):
    Like = apps.get_model('common', 'Like')
    like = Like.objects.filter(to_photo_id=photo_id).first()

    if like:
        like.delete()
    else:
        like = Like(to_photo_id=photo_id)
        like.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}" )


def copy_link_to_clipboard(request, photo_id):
    copy(request.META["HTTP_HOST"] + resolve_url('photo_details_page', photo_id))

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")

