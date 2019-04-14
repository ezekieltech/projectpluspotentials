from django import template

register = template.Library()


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    special_letters = ['&', '/', ' ']
    for i in special_letters:
        arg1 = str(arg1).replace(i, '')
        arg2 = str(arg2).replace(i, '')
    return arg1 + arg2


@register.filter
def mycounter(a):
    """variable to hold counter"""
    mycount = 0
    mycount = + 1
    return mycount
