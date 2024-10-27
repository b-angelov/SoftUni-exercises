from django.urls import path

from regular_exam_project_27102024.authors.views import AuthorCreateView, AuthorDetailsView, AuthorEditView, \
    AuthorDeleteView

urlpatterns = [
    path('create/', AuthorCreateView.as_view(), name='author-create'),
    path('details/', AuthorDetailsView.as_view(), name='author_details'),
    path('edit/', AuthorEditView.as_view(), name='author-edit'),
    path('delete/', AuthorDeleteView.as_view(), name='author-delete')
]
