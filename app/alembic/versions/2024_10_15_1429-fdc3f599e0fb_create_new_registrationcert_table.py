"""create new RegistrationCert Table

Revision ID: fdc3f599e0fb
Revises: 
Create Date: 2024-10-15 14:29:30.676409

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "fdc3f599e0fb"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "registration_certificates",
        sa.Column("trade_Name", sa.String(), nullable=False),
        sa.Column("reg_Cert_Number", sa.String(), nullable=False),
        sa.Column("createAt_Reg_Cer", sa.DateTime(), nullable=False),
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.PrimaryKeyConstraint("id"),
        sa.UniqueConstraint("reg_Cert_Number"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("registration_certificates")
    # ### end Alembic commands ###