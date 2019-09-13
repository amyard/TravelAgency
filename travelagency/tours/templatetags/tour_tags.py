from django import template
from location.models import Country

register = template.Library()


# TODO - как узнать модель
# TODO - как отработаем с редактором


@register.simple_tag
def trans_fields(pk, field, lang):
    curr_field = field if lang=='ru' else f'{field}_{lang}'
    res = getattr(Country.objects.get(id=pk), curr_field)
    return res