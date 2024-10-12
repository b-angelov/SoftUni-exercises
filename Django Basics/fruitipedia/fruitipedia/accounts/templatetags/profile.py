from django import template

from fruitipedia.accounts.models import Profile

register = template.Library()


@register.simple_tag
def profile():
    return Profile.get_last_profile()
