"""Added document relationships

Revision ID: 0003
Revises: 0002
Create Date: 2022-08-30 12:17:19.702267

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "0003"
down_revision = "0002"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "relationship",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("type", sa.Text(), nullable=False),
        sa.Column("name", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_relationship")),
    )
    op.create_table(
        "document_relationship",
        sa.Column("document_id", sa.Integer(), nullable=False),
        sa.Column("relationship_id", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["document_id"],
            ["document.id"],
            name=op.f("fk_document_relationship__document_id__document"),
            ondelete="CASCADE",
        ),
        sa.ForeignKeyConstraint(
            ["relationship_id"],
            ["relationship.id"],
            name=op.f("fk_document_relationship__relationship_id__relationship"),
            ondelete="CASCADE",
        ),
        sa.PrimaryKeyConstraint(
            "document_id", "relationship_id", name=op.f("pk_document_relationship")
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("document_relationship")
    op.drop_table("relationship")
    # ### end Alembic commands ###
