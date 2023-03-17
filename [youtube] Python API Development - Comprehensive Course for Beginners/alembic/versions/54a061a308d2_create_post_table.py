"""create post table

Revision ID: 54a061a308d2
Revises: 
Create Date: 2023-03-16 22:11:12.252446

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54a061a308d2'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(),
                              nullable=False, primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
