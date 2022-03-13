import ormar

from app.db.base_class import MainMeta
from app.models.filefield import ImageField


class Profile(ormar.Model):
    class Meta(MainMeta):
        pass
    id: int = ormar.Integer(primary_key=True)
    avatar: ImageField = ormar.ForeignKey(ImageField, ondelete='CASCADE')
    full_name: str = ormar.String(max_length=255, nullable=True)

