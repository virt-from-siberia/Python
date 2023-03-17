"""add user table

Revision ID: 347479fab8d7
Revises: 56da5f38bc33
Create Date: 2023-03-17 14:57:21.077408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '347479fab8d7'
down_revision = '56da5f38bc33'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'),
                              nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'),
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
