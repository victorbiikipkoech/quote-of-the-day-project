"""empty message

Revision ID: 3ea6967a8498
Revises: 
Create Date: 2024-02-08 15:13:22.145290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3ea6967a8498'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('authors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('nationality', sa.String(length=150), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('quotes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('text', sa.String(length=150), nullable=False),
    sa.Column('author_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['author_id'], ['authors.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('text')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('quotes')
    op.drop_table('categories')
    op.drop_table('authors')
    # ### end Alembic commands ###
