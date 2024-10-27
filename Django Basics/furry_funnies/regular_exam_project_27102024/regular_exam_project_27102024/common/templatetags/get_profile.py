

from django import template

from regular_exam_project_27102024.authors.models import Author

register = template.Library()


@register.simple_tag
def profile():
    return Author.objects.last()
