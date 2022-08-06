"""create post table

Revision ID: 707e5c371f64
Revises: 
Create Date: 2022-08-06 13:28:52.667658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '707e5c371f64'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer, nullable=False, primary_key=True),
                    sa.Column('title', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
