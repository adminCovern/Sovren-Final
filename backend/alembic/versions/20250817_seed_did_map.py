"""seed executive_did_map with founder C-Suite DIDs

Revision ID: 20250817_seed_did_map
Revises: 20250817_telephony_map
Create Date: 2025-08-17
"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "20250817_seed_did_map"
down_revision = "20250817_telephony_map"
branch_labels = None
depends_on = None

# Table definition (matches your models/telephony.py)
executive_did_map = sa.table(
    "executive_did_map",
    sa.column("did", sa.String),
    sa.column("persona", sa.String),
    sa.column("cnam", sa.String),
)

SEED = [
    {"did": "15306885012", "persona": "CFO", "cnam": "COVREN CFO"},
    {"did": "15306885015", "persona": "COO", "cnam": "COVREN COO"},
    {"did": "15306885017", "persona": "CTO", "cnam": "COVREN CTO"},
    {"did": "15306885023", "persona": "CMO", "cnam": "COVREN CMO"},
    {"did": "15306885024", "persona": "CLO", "cnam": "COVREN CLO"},
    {"did": "15306885025", "persona": "CRO", "cnam": "COVREN CRO"},
    {"did": "15306885034", "persona": "CHRO", "cnam": "COVREN CHRO"},
    {"did": "15306885066", "persona": "COS", "cnam": "COVREN COS"},
]

def upgrade() -> None:
    op.bulk_insert(executive_did_map, SEED)


def downgrade() -> None:
    conn = op.get_bind()
    for row in SEED:
        conn.execute(
            sa.text("DELETE FROM executive_did_map WHERE did = :did"),
            {"did": row["did"]},
        )
