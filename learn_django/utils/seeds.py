import connect
from models import Authors, Qoutes

import json
import random


def generate_unique_id():
    return random.randint(1, 1000000)


with open("authors.json", errors="ignore") as f:
    file_data = json.load(f)

for item in file_data:
    Authors(**item, _id=generate_unique_id()).save()

with open("quotes.json", errors="ignore") as f:
    file_data = json.load(f)

for item in file_data:
    qoute = Qoutes(
        _id=generate_unique_id(),
        tags=item["tags"],
        quote=item["quote"],
    )

    find_author = Authors.objects(fullname=item["author"])
    if find_author.count() >= 1:
        qoute.author = find_author[0]

    qoute.save()
