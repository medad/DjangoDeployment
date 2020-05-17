from django import template

register = template.Library()

@register.filter(name='cut_string') # gai: you can use decorators

def cut_string(value, arg):
  return value.replace(arg,'')

# register.filter('cut_string',cut_string) # gai: you can use decorators