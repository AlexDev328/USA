import databases
import ormar
import sqlalchemy

from app.core.config import settings

metadata = sqlalchemy.MetaData()
database = databases.Database(settings.SQLALCHEMY_DATABASE_URI)


class MainMeta(ormar.ModelMeta):
    metadata = metadata
    database = database
