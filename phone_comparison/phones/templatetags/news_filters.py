from django import template



register = template.Library()

@register.filter
def check_value(in_value):
    if isinstance(in_value, bool) and in_value:
        out_value = 'Есть'
    elif isinstance(in_value, bool) and not in_value:
        out_value = 'Нет'
    elif in_value is None:
        out_value = '-'
    else:
        out_value = in_value
    return out_value






