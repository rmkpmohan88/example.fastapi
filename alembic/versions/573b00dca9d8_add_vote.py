"""add vote

Revision ID: 573b00dca9d8
Revises: db8938b1f291
Create Date: 2022-08-06 15:14:38.757078

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '573b00dca9d8'
down_revision = '53cc0190a6ac'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('votes',
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.Column('post_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(
                        ['post_id'], ['posts.id'], ondelete='CASCADE'),
                    sa.ForeignKeyConstraint(
                        ['user_id'], ['users.id'], ondelete='CASCADE'),
                    sa.PrimaryKeyConstraint('user_id', 'post_id'))
    pass


def downgrade() -> None:
    op.drop_table('votes')
    pass
