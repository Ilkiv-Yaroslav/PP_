"""create account table

Revision ID: 0cdfdb11eb73
Revises: 
Create Date: 2022-12-02 00:46:25.943066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cdfdb11eb73'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('User',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(length=100), nullable=False),
                    sa.Column('firstName', sa.String(length=100), nullable=True),
                    sa.Column('lastName', sa.String(length=100), nullable=True),
                    sa.Column('email', sa.String(length=100), nullable=True),
                    sa.Column('password', sa.String(length=100), nullable=False),
                    sa.Column('phone', sa.String(length=100), nullable=True),
                    sa.Column('userStatus', sa.String(length=100), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('Student',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=100), nullable=False),
                    sa.Column('lastName', sa.String(length=100), nullable=False),
                    sa.Column('avarageMark', sa.Integer(), nullable=True),
                    sa.Column('User_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['User_id'], ['User.id'], ),
                    sa.PrimaryKeyConstraint('id', 'User_id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('Student')
    op.drop_table('User')
    # ### end Alembic commands ###
