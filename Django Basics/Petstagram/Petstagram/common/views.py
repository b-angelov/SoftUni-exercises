from django.apps import apps
from django.core.exceptions import ValidationError
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.shortcuts import render, redirect, resolve_url
from django.views.generic import ListView
from prompt_toolkit.search import SearchState
from pyperclip import copy


# Create your views here.
class ClassImporter:

    @property
    def CommentForm(self):
        from Petstagram.common.forms import CommentForm
        return CommentForm

    @property
    def SearchForm(self):
        from Petstagram.common.forms import SearchForm
        return SearchForm

    @property
    def Photo(self):
        from Petstagram.photos.models import Photo
        return Photo

class HomePageView(ListView):
    model = ClassImporter.Photo
    template_name = 'common/home-page.html'
    context_object_name = "photos"
    paginate_by = 2
    COMMENT_FORM =ClassImporter.CommentForm
    SEARCH_FORM = ClassImporter.SearchForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["url"] = self.request.get_full_path()
        context["comment_form"] = self.COMMENT_FORM()
        context["search_form"] = self.SEARCH_FORM()
        context["search_string"] = self.request.GET.get("pet_name")
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        pet_name = self.request.GET.get('pet_name')

        if pet_name:
            queryset = queryset.filter(tagged_pets__name__icontains=pet_name)

        return queryset

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

    photos_per_page = 1
    paginator = Paginator(photos, photos_per_page)
    page = request.GET.get('page')

    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)


    context = {
        'photos': photos,
        'url': details_url,
        "comment_form":comment_form,
        "search_form": search_form,
        "search_string": request.GET.get('pet_name'),
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


