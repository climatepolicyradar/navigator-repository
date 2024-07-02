"""Add valid_metadata field to family document model

Revision ID: 0040
Revises: 0039
Create Date: 2024-07-01 17:34:26.909964

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0040"
down_revision = "0039"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "family_document",
        sa.Column(
            "valid_metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=True
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("family_document", "valid_metadata")
    # ### end Alembic commands ###
