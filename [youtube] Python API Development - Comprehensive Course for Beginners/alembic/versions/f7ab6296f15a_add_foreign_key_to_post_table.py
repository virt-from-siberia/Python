"""add foreign key to post table

Revision ID: f7ab6296f15a
Revises: 347479fab8d7
Create Date: 2023-03-17 17:24:20.687355

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f7ab6296f15a'
down_revision = '347479fab8d7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key(
        'posts_users-fk', source_table="posts", referent_table="users",
        local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('posts_users-fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
