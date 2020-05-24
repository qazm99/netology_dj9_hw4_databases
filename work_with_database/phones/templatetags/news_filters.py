from django import template



register = template.Library()

@register.filter
def lte_exist(in_lte):
    if in_lte == True:
        out_lte = 'Есть'
    else:
        out_lte = 'Нет'
    return out_lte






