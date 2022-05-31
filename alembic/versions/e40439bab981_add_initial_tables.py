"""Add initial tables

Revision ID: e40439bab981
Revises:
Create Date: 2022-05-31 02:22:56.889100+00:00

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "e40439bab981"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "challenge",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "developer",
        sa.Column("id", sa.Integer(), nullable=True),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column(
            "country", sqlmodel.sql.sqltypes.AutoString(), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "developer_mcq_score",
        sa.Column("dev_id", sa.Integer(), nullable=True),
        sa.Column("challenge_id", sa.Integer(), nullable=True),
        sa.Column("rank_percentile", sa.Float(), nullable=False),
        sa.Column("passed", sa.Boolean(), nullable=False),
        sa.Column("updated_date", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["challenge_id"],
            ["challenge.id"],
        ),
        sa.ForeignKeyConstraint(
            ["dev_id"],
            ["developer.id"],
        ),
        sa.PrimaryKeyConstraint("dev_id", "challenge_id"),
    )

def downgrade():
    op.drop_table("developer_mcq_score")
    op.drop_table("developer")
    op.drop_table("challenge")
