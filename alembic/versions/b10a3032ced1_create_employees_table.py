"""Create employees table

Revision ID: b10a3032ced1
Revises: 
Create Date: 2024-08-03 11:34:01.163685
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b10a3032ced1'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('phone', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_employees_email'), 'employees', ['email'], unique=True)
    op.create_index(op.f('ix_employees_id'), 'employees', ['id'], unique=False)
    op.create_index(op.f('ix_employees_name'), 'employees', ['name'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_employees_name'), table_name='employees')
    op.drop_index(op.f('ix_employees_id'), table_name='employees')
    op.drop_index(op.f('ix_employees_email'), table_name='employees')
    op.drop_table('employees')
    # ### end Alembic commands ###