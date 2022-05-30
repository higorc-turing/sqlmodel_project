"""Add initial tables

Revision ID: 5929e04ea844
Revises:
Create Date: 2022-05-30 02:18:44.269601+00:00

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '5929e04ea844'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### Adjusted commands ###
    op.create_table('challenge',
        sa.Column('id', sa.Integer(), nullable=True),
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('developer',
        sa.Column('id', sa.Integer(), nullable=True),
        sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column('country', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('developer_mcq_score',
        sa.Column('dev_id', sa.Integer(), nullable=True),
        sa.Column('challenge_id', sa.Integer(), nullable=True),
        sa.Column('rank_percentile', sa.Float(), nullable=False),
        sa.Column('passed', sa.Boolean(), nullable=False),
        sa.Column('updated_date', sa.DateTime(), nullable=True),
        sa.ForeignKeyConstraint(['challenge_id'], ['challenge.id'], ),
        sa.ForeignKeyConstraint(['dev_id'], ['developer.id'], ),
        sa.PrimaryKeyConstraint('dev_id', 'challenge_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('developer_mcq_score')
    op.drop_table('developer')
    op.drop_table('challenge')
    # ### end Alembic commands ###