from django import template
from Main.models import *

register = template.Library()


@register.simple_tag(name='getcats')
def get_categories(filter=None):
    if not filter:
        return Category.objects.all()
    else:
        return Category.objects.filter(pk=filter)


@register.inclusion_tag('Main/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.order_by(sort)

    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag('Main/list_posts.html')
def show_posts(sort=None, cat_selected=0):
    if not sort:
        posts = Main.objects.all()
    else:
        posts = Main.objects.order_by(sort)

    return {"posts": posts, "cat_selected": cat_selected}
