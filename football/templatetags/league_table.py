__author__ = 'brett'
from django.core.urlresolvers import reverse
from django import template


register = template.Library()


@register.inclusion_tag('football/leaguetable_js.html')
def league_table_js(start_year):

    return {
        'data_endpoint': reverse('football:api:matches-list') + '?season={}'.format(start_year)
    }


@register.inclusion_tag('football/leaguetable_controls.html')
def league_table_controls():
    return {}
