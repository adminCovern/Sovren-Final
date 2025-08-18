"""seed executive_did_map with founder C-Suite DIDs

Revision ID: 20250817_seed_did_map
Revises: 20250817_telephony_map
Create Date: 2025-08-17
"""
from alembic import op

# revision identifiers, used by Alembic.
revision = '20250817_seed_did_map'
down_revision = '20250817_telephony_map'
branch_labels = None
depends_on = None

SEED = [
    ("15306885012", "CFO", "COVREN CFO"),
    ("15306885015", "COO", "COVREN COO"),
    ("15306885017", "CTO", "COVREN CTO"),
    ("15306885023", "CMO", "COVREN CMO"),
    ("15306885024", "CLO", "COVREN CLO"),
    ("15306885025", "CRO", "COVREN CRO"),
    ("15306885034", "CHRO", "COVREN CHRO"),
    ("15306885066", "COS", "COVREN COS"),
]

def upgrade() -> None:
    for did, persona, cnam in SEED:
        op.execute(
            """
            INSERT INTO executive_did_map(did, persona, cnam)
            VALUES ('{did}', '{persona}', '{cnam}')
            ON CONFLICT (did) DO NOTHING;
            """.format(did=did, persona=persona, cnam=cnam)
        )


def downgrade() -> None:
    for did, _, _ in SEED:
        op.execute("DELETE FROM executive_did_map WHERE did = '{}';".format(did))

