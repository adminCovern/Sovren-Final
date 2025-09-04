"""create executive_did_map

Revision ID: 20250817_telephony_map
Revises: d678d7eb7b05
Create Date: 2025-08-17
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '20250817_telephony_map'
down_revision = 'd678d7eb7b05'
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.create_table(
        'executive_did_map',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('did', sa.String(length=20), nullable=False),
        sa.Column('persona', sa.String(length=64), nullable=False),
        sa.Column('cnam', sa.String(length=64), nullable=False),
    )
    op.create_unique_constraint('uq_executive_did_map_did', 'executive_did_map', ['did'])
    op.create_index('ix_executive_did_map_did', 'executive_did_map', ['did'])


def downgrade() -> None:
    op.drop_index('ix_executive_did_map_did', table_name='executive_did_map')
    op.drop_constraint('uq_executive_did_map_did', 'executive_did_map', type_='unique')
    op.drop_table('executive_did_map')
