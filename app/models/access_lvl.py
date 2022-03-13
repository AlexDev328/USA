import ormar
from app.db.base_class import MainMeta


class AccessLvl(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    name: str = ormar.String(max_length=100, unique=True)
    code = ormar.Integer(nullable=False)
