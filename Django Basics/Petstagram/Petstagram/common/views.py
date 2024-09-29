from django.apps import apps
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from pyperclip import copy



# Create your views here.

def index(request):
    from Petstagram.common.forms import CommentForm
    from Petstagram.common.forms import SearchForm

    comment_form = CommentForm(request.POST or None)
    Photo = apps.get_model('photos', 'Photo')
    details_url = request.get_full_path()
    search_form = SearchForm(request.GET or None)

    if search_form and search_form.is_valid():
        photos = Photo.objects.filter(tagged_pets__name__icontains=search_form.cleaned_data["pet_name"])
    else:
        photos = Photo.get_all_photos()

    context = {
        'photos': photos,
        'url': details_url,
        "comment_form":comment_form,
        "search_form": search_form,
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

def add_comment(request, photo_id):
    from Petstagram.common.models import Comment
    from Petstagram.common.forms import CommentForm
    comment = Comment(to_photo_id=photo_id)

    if request.method == "POST":
        form = CommentForm(request.POST or None, instance=comment)
        if form.is_valid():
            form.save()

    return redirect(request.META["HTTP_REFERER"] + f"#{photo_id}")


