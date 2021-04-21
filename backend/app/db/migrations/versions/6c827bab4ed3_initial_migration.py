"""initial_migration

Revision ID: 6c827bab4ed3
Revises: 
Create Date: 2021-04-21 19:01:15.571402

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic
revision = '6c827bab4ed3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table("users",
        sa.Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
        sa.Column("email", sa.String(), nullable=False, index=True),
        sa.Column("hashed_password", sa.String(), nullable=True),
        sa.Column("first_name", sa.String(), nullable=True),
        sa.Column("last_name", sa.String(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True)
    )


def downgrade() -> None:
    op.drop_table("users")

