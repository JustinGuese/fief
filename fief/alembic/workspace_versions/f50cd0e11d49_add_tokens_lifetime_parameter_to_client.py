"""Add tokens lifetime parameter to Client

Revision ID: f50cd0e11d49
Revises: 31f6171a84fa
Create Date: 2023-01-16 13:09:39.792996

"""
import sqlalchemy as sa
from alembic import op

import fief
from fief.settings import settings

# revision identifiers, used by Alembic.
revision = "f50cd0e11d49"
down_revision = "31f6171a84fa"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "fief_clients",
        sa.Column(
            "authorization_code_lifetime_seconds",
            sa.Integer(),
            nullable=False,
            server_default=str(settings.default_authorization_code_lifetime_seconds),
        ),
    )
    op.add_column(
        "fief_clients",
        sa.Column(
            "access_id_token_lifetime_seconds",
            sa.Integer(),
            nullable=False,
            server_default=str(settings.default_access_id_token_lifetime_seconds),
        ),
    )
    op.add_column(
        "fief_clients",
        sa.Column(
            "refresh_token_lifetime_seconds",
            sa.Integer(),
            nullable=False,
            server_default=str(settings.default_refresh_token_lifetime_seconds),
        ),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("fief_clients", "refresh_token_lifetime_seconds")
    op.drop_column("fief_clients", "access_id_token_lifetime_seconds")
    op.drop_column("fief_clients", "authorization_code_lifetime_seconds")
    # ### end Alembic commands ###
