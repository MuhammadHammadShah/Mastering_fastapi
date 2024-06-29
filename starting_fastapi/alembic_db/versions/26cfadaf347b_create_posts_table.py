"""create posts table

Revision ID: 26cfadaf347b
Revises: 
Create Date: 2024-06-29 16:48:05.387056

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '26cfadaf347b'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts' , sa.Column('id' , sa.Integer() , nullable=False , primary_key=True) , sa.Column('title' , sa.String() , nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
