"""add last few colums to posts table

Revision ID: 6ffb9611c8ed
Revises: f7ab6296f15a
Create Date: 2023-03-17 18:10:02.901855

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6ffb9611c8ed'
down_revision = 'f7ab6296f15a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default='TRUE'),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    pass
