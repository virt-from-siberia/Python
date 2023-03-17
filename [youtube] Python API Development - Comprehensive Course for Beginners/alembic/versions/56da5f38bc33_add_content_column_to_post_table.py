"""add content column to post table

Revision ID: 56da5f38bc33
Revises: 54a061a308d2
Create Date: 2023-03-17 14:44:09.150282

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56da5f38bc33'
down_revision = '54a061a308d2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
