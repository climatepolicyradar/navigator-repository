"""Drop FamilyDocumentType table

Revision ID: 0050
Revises: 0049
Create Date: 2024-07-17 17:23:02.844980

"""

from alembic import op

# revision identifiers, used by Alembic.
revision = "0050"
down_revision = "0049"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(
        "fk_family_document__document_type__family_document_type",
        "family_document",
        type_="foreignkey",
    )
    op.drop_column("family_document", "document_type")
    op.drop_table("family_document_type")
    # ### end Alembic commands ###


def downgrade():
    # There is no way back.
    pass
