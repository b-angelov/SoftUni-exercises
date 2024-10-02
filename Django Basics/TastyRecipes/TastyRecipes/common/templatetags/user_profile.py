from django import template

from TastyRecipes.accounts.models import Profile

register = template.Library()

@register.simple_tag
def user_profile():
    profile = Profile.get_last_profile()
    return profile