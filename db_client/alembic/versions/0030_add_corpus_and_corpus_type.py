"""Add Corpus and Corpus Type

Revision ID: 0030
Revises: 0029
Create Date: 2024-03-20 15:12:54.844580

"""

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "0030"
down_revision = "0029"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "corpus_type",
        sa.Column("value", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column(
            "valid_metadata", postgresql.JSONB(astext_type=sa.Text()), nullable=False
        ),
        sa.PrimaryKeyConstraint("value", name=op.f("pk_corpus_type")),
    )
    op.create_table(
        "corpus",
        sa.Column("import_id", sa.Text(), nullable=False),
        sa.Column("title", sa.Text(), nullable=False),
        sa.Column("description", sa.Text(), nullable=False),
        sa.Column("organisation_id", sa.Integer(), nullable=False),
        sa.Column("corpus_type", sa.Text(), nullable=False),
        sa.ForeignKeyConstraint(
            ["corpus_type"],
            ["corpus_type.value"],
            name=op.f("fk_corpus__corpus_type__corpus_type"),
        ),
        sa.ForeignKeyConstraint(
            ["organisation_id"],
            ["organisation.id"],
            name=op.f("fk_corpus__organisation_id__organisation"),
        ),
        sa.PrimaryKeyConstraint("import_id", name=op.f("pk_corpus")),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("corpus")
    op.drop_table("corpus_type")
    # ### end Alembic commands ###
