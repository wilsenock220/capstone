'''
Custom tag to display the latest articles
wherever I choose to load them.
'''

from django import template

from ..models import Article

register = template.Library()

@register.simple_tag
def latest_articles():
    # Return last 3 articles
    articles = Article.objects.all()
    return articles[0:3]
