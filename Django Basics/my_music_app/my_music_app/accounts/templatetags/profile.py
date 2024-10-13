from django import template

from my_music_app.accounts.models import Profile

register = template.Library()


@register.simple_tag
def profile():
    return Profile.get_last_profile()
