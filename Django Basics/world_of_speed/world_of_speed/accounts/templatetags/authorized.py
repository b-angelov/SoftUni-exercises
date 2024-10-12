from django import template

from world_of_speed.accounts.models import Profile

register = template.Library()


@register.simple_tag
def authorized():
    return Profile.objects.last()
