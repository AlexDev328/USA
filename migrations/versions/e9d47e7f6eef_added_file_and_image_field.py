"""added file and image field

Revision ID: e9d47e7f6eef
Revises: ce08fa37ff62
Create Date: 2022-02-04 19:42:10.961475

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e9d47e7f6eef'
down_revision = 'ce08fa37ff62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('imagefields')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('imagefields',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('filename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('url', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='imagefields_pkey'),
    sa.UniqueConstraint('filename', name='imagefields_filename_key'),
    sa.UniqueConstraint('url', name='imagefields_url_key')
    )
    # ### end Alembic commands ###
