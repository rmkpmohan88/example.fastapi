"""add phone number

Revision ID: ae2ceca810af
Revises: 573b00dca9d8
Create Date: 2022-08-06 15:26:55.360173

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ae2ceca810af'
down_revision = '573b00dca9d8'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('users', sa.Column('phone_number', sa.String, nullable=True))
    pass


def downgrade() -> None:
    op.drop_column('users', 'phone_number')
    pass
