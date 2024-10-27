from django.urls import path, include

from regular_exam_project_27102024.posts.views import PostCreateView, PostDetailsView, PostEditView, PostDeleteView

urlpatterns = [
    path('create/', PostCreateView.as_view(), name='post-create'),
    path('<int:post_id>/', include(
        [
            path('details/', PostDetailsView.as_view(), name='post-details'),
            path('edit/', PostEditView.as_view(), name='post-edit'),
            path('delete/', PostDeleteView.as_view(), name='post-delete'),
        ]
    )),
]
