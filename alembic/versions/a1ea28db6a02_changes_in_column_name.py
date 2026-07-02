"""changes in column name

Revision ID: a1ea28db6a02
Revises: 0dca52b0bd25
Create Date: 2026-07-02 20:53:39.770968

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1ea28db6a02'
down_revision: Union[str, Sequence[str], None] = '0dca52b0bd25'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    with op.batch_alter_table("users") as batch_op:

        batch_op.alter_column(
            "id",
            new_column_name="user_id"
        )

        batch_op.alter_column(
            "Email_id",
            new_column_name="email_id"
        )

        batch_op.alter_column(
            "User_name",
            new_column_name="user_name"
        )

        batch_op.alter_column(
            "Password_hash",
            new_column_name="password_hash"
        )

def downgrade() -> None:
    with op.batch_alter_table("users") as batch_op:

        batch_op.alter_column(
            "user_id",
            new_column_name="id"
        )

        batch_op.alter_column(
            "email_id",
            new_column_name="Email_id"
        )

        batch_op.alter_column(
            "user_name",
            new_column_name="User_name"
        )

        batch_op.alter_column(
            "password_hash",
            new_column_name="Password_hash"
        )