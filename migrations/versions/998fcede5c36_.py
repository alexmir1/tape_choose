"""empty message

Revision ID: 998fcede5c36
Revises: 
Create Date: 2017-10-06 22:42:59.683409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '998fcede5c36'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('color',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('image_link', sa.String(length=128), nullable=True),
    sa.Column('hex', sa.String(length=8), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('image_link')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=False),
    sa.Column('grade', sa.String(length=4), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=False),
    sa.Column('feedback_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_grade'), 'user', ['grade'], unique=False)
    op.create_table('mark',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('mark', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('color_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['color_id'], ['color.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mark')
    op.drop_index(op.f('ix_user_grade'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_table('color')
    # ### end Alembic commands ###
