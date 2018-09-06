from django import template
from django.urls import reverse
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.urls import NoReverseMatch

import re


register = template.Library()


def localurl(match):
  string = match.group()
  # Strip off the {{ and }}
  string = string[2:-2]
  # Separate the link type and the id
  link_text, link = string.split("|")
  link_type, link_id = link.split(":")
  link_url = reverse('elements:'+link_type, args=(link_id,))
  return '<a href={}>{}</a>'.format(link_url, link_text)


@register.filter
def internal_links(value):
  """
  Filter for internal links in the format
  {{<text>|<type>:<id>}}, i.e.{{ImageNet|paper:1}}.
  """
  value = conditional_escape(value)
  try:
    pattern = '{{.+?\|\S+?:\S+?}}'
    p = re.compile(pattern)
    return mark_safe(p.sub(localurl, value))
  except NoReverseMatch as e:
    return '[[Link error: {}]]'.format(e.args[0])
