from django import template

register = template.Library()

@register.filter(name='split_string')
def split(value,key):
	return value.split(key)
