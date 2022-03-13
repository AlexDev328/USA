from typing import Optional

import ormar
from app.db.base_class import MainMeta


class FileField(ormar.Model):
    class Meta(MainMeta):
        abstract = True
        path = ''

    id: int = ormar.Integer(primary_key=True)
    filename: str = ormar.String(max_length=100, unique=True)
    url: str = ormar.String(max_length=255, unique=True)


class ImageField(FileField):
    class Meta(MainMeta):
        path = 'images'
