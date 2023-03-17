"""add last few colums to posts table additional

Revision ID: ac9b1af1f922
Revises: 6ffb9611c8ed
Create Date: 2023-03-17 21:01:06.515860

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ac9b1af1f922'
down_revision = '6ffb9611c8ed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False,
        server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'created_at')
    pass
