from bson.objectid import ObjectId

from django import template

from utils import connect
from utils.models import Authors, Qoutes

register = template.Library()


def get_author_fullname(AuthorObj):
    return AuthorObj["fullname"]


register.filter("author", get_author_fullname)
