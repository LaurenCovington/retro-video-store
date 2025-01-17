"""empty message

Revision ID: 22247be4f0b8
Revises: 855ad2c04789
Create Date: 2021-05-20 18:10:43.305421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22247be4f0b8'
down_revision = '855ad2c04789'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rental',
    sa.Column('rental_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=True),
    sa.Column('video_id', sa.Integer(), nullable=True),
    sa.Column('check_out_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['customer_id'], ['customer.customer_id'], ),
    sa.ForeignKeyConstraint(['video_id'], ['video.video_id'], ),
    sa.PrimaryKeyConstraint('rental_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('rental')
    # ### end Alembic commands ###
