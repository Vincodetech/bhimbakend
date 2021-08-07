from django import template
from home.models import *

register = template.Library()

@register.filter(name='newsbycat')
def newsbycat(id):
    news_by_category = News.objects.filter(category=id)
    return {'news_by_category': news_by_category}