"""add content column to posts table

Revision ID: 3ddee76c3eff
Revises: 26cfadaf347b
Create Date: 2024-06-29 16:52:21.215047

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3ddee76c3eff'
down_revision: Union[str, None] = '26cfadaf347b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
