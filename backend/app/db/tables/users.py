import sqlalchemy
from sqlalchemy.dialects import postgresql
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime

metadata = sqlalchemy.MetaData()


users_table = sqlalchemy.Table(
    "users",
    metadata,
    Column("id", postgresql.UUID(as_uuid=True), primary_key=True),
    Column("email", String(), nullable=False, index=True),
    Column("hashed_password", String(), nullable=True),
    Column("first_name", String(), nullable=True),
    Column("last_name", String(), nullable=True),
    Column("created_at", DateTime(), nullable=True)
)