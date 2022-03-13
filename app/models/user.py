import ormar
from app.db.base_class import MainMeta
from app.models.access_lvl import AccessLvl
from app.models.profile import Profile


class User(ormar.Model):
    class Meta(MainMeta):
        pass

    id: int = ormar.Integer(primary_key=True)
    username: str = ormar.String(max_length=100, unique=True)
    email: str = ormar.String(index=True, unique=True, nullable=False, max_length=255)
    is_active: bool = ormar.Boolean(default=True, nullable=False)
    is_superuser: bool = ormar.Boolean(default=False, nullable=False)
    access: AccessLvl = ormar.ForeignKey(AccessLvl, ondelete=None, nullable=True)
    hashed_password = ormar.String(max_length=255, unique=False)
    profile: Profile = ormar.ForeignKey(Profile, ondelete="CASCADE", nullable=True)
