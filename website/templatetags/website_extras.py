from django import template
from django.core.urlresolvers import reverse
import re

register = template.Library()

@register.simple_tag
def url_no_i18n(viewname, *args, **kwargs):
    result = reverse(viewname, *args, **kwargs)
    m = re.match(r'(/[^/]*)(/.*$)', result)
    return m.groups()[1]
