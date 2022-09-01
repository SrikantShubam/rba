from urllib import request
from django import template
import requests
register = template.Library()

@register.simple_tag
def setvar(val=None):
  return request.user