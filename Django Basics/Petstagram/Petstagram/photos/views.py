from django.apps import apps
from django.shortcuts import render, redirect

# Create your views here.

def photo_add(request):
    from Petstagram.photos.forms import PhotoCreateForm

    form = PhotoCreateForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect("home_page")

    context = {
        "form": form,
    }

    return render(request, 'photos/photo-add-page.html', context)

def photo_details(request, pk):
    Photo = apps.get_model('photos', 'Photo')
    photo = Photo.get_photo_by_id(pk)
    comments = photo.comment_set.all()
    likes = photo.like_set.count()

    context = {
        'photo':photo,
        'comments':comments,
        'likes':likes,
    }

    return render(request, 'photos/photo-details-page.html', context)

def photo_edit(request, pk):
    from Petstagram.photos.forms import PhotoEditForm
    from Petstagram.photos.models import Photo
    photo = Photo.objects.get(pk=pk)

    if request.method == "GET":
        form = PhotoEditForm(instance=photo, initial=photo.__dict__)
    else:
        form = PhotoEditForm(request.POST or None, instance=photo)
        if form.is_valid():
            form.save()
            return redirect("photo_details_page", pk=pk)

    context = {
        "form":form
    }

    return render(request, 'photos/photo-edit-page.html', context)


def photo_delete(request, pk):
    from Petstagram.photos.models import Photo
    photo = Photo.get_photo_by_id(pk)

    photo.delete()
    return redirect("home_page")
