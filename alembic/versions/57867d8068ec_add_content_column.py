"""add content column

Revision ID: 57867d8068ec
Revises: 707e5c371f64
Create Date: 2022-08-06 13:47:48.507470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '57867d8068ec'
down_revision = '707e5c371f64'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
