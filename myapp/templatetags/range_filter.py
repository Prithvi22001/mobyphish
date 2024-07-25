from django import template

register = template.Library()

@register.filter
def times(number):
    return range(number)


@register.filter
def neg_times(number):
    return range(5-number)