from django import template

from MyPlant.accounts.models import Profile

register = template.Library()

@register.simple_tag
def profile():
    return Profile.objects.last()