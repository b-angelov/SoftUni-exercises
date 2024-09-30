from django import template
register = template.Library()

@register.simple_tag
def page_url(page=1, pet_name=None, url = ''):
    url += f"?page={page}" + (f"&pet_name={pet_name}" if pet_name else "")
    return url