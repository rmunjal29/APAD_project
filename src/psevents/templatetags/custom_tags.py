from django import template
register = template.Library()

from ..models import *




@register.filter(name='dict_key')
def dict_key(d):
    '''Returns the given key from a dictionary.'''
    return list(d)[0][1]