from django import template

register = template.Library()

'''
@register.filter
def mycounter(forloop.counter, service, *args, **kwargs):
    """variable to hold counter"""
    first = [a]
    if project.service = service:
        mycount = 0
        return mycount
    mycount = 0
    return mycount

'''
