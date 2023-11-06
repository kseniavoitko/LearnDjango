from mongoengine import *


class Authors(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()


class Qoutes(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
