"""create RegisterCert model

Revision ID: a3e3c59253b5
Revises: 
Create Date: 2024-10-10 14:56:32.535378

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "a3e3c59253b5"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "registration_certificates",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("trade_Name", sa.String(), nullable=False),
        sa.Column("reg_Cert_Number", sa.String(), nullable=False),
        sa.Column("createAt_Reg_Cer", sa.String(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("reg_Cert_Number"),
    )
    op.create_index(
        op.f("ix_registration_certificates_id"),
        "registration_certificates",
        ["id"],
        unique=False,
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_registration_certificates_id"),
        table_name="registration_certificates",
    )
    op.drop_table("registration_certificates")
    # ### end Alembic commands ###