"""create users table fixed

Revision ID: a6b868dd9f7c
Revises: 
Create Date: 2026-01-20 14:36:55.911698
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'a6b868dd9f7c'
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    """Upgrade schema: create users table."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.DateTime, server_default=sa.func.now(), nullable=False),
        sa.Column('updated_at', sa.DateTime, server_default=sa.func.now(), onupdate=sa.func.now(), nullable=False)
    )

def downgrade() -> None:
    """Downgrade schema: drop users table."""
    op.drop_table('users')

