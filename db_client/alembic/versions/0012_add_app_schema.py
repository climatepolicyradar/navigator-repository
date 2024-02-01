"""add app schema

Revision ID: 0012
Revises: 0011
Create Date: 2023-01-31 21:52:10.301044

"""
from alembic import op
from alembic.op import execute
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0012'
down_revision = '0011'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_admin'))
    )
    op.create_index(op.f('ix_admin_email'), 'admin', ['email'], unique=True)
    op.create_table('organisation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('organisation_type', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_organisation'))
    )
    op.create_table('admin_organisation',
    sa.Column('admin_id', sa.Integer(), nullable=False),
    sa.Column('organisation_id', sa.Integer(), nullable=False),
    sa.Column('job_title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['admin_id'], ['admin.id'], name=op.f('fk_admin_organisation__admin_id__admin')),
    sa.ForeignKeyConstraint(['organisation_id'], ['organisation.id'], name=op.f('fk_admin_organisation__organisation_id__organisation')),
    sa.PrimaryKeyConstraint('admin_id', 'organisation_id', name=op.f('pk_admin_organisation'))
    )
    op.drop_column('physical_document_language', 'id')
    # ### end Alembic commands ###
    execute("alter table physical_document_language ADD CONSTRAINT pk_physical_document_language PRIMARY KEY (language_id, document_id)")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('physical_document_language', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_table('admin_organisation')
    op.drop_table('organisation')
    op.drop_index(op.f('ix_admin_email'), table_name='admin')
    op.drop_table('admin')
    # ### end Alembic commands ###
