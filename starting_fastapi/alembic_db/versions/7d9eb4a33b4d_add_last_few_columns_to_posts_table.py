"""add last few columns to posts table

Revision ID: 7d9eb4a33b4d
Revises: 86517178e6c7
Create Date: 2024-06-29 17:19:47.250630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7d9eb4a33b4d'
down_revision: Union[str, None] = '86517178e6c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts' , sa.Column('published' , sa.Boolean() , nullable=False , server_default='TRUE'),)
    op.add_column('posts' , sa.Column('created_at' , sa.TIMESTAMP(timezone=True) , nullable=False , server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts' , 'published')
    op.drop_column('posts' , 'created_at')
    pass
