"""add user table

Revision ID: 2798f7d578fe
Revises: 57867d8068ec
Create Date: 2022-08-06 13:54:41.539053

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2798f7d578fe'
down_revision = '57867d8068ec'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email'))
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
