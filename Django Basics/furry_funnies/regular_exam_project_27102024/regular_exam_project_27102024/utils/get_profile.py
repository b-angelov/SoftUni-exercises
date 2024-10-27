from regular_exam_project_27102024.authors.models import Author


def get_profile():
    return Author.objects.last()