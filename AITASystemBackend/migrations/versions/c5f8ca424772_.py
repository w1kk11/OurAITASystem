"""empty message

Revision ID: c5f8ca424772
Revises: 770211ecef22
Create Date: 2024-05-02 20:33:14.178957

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5f8ca424772'
down_revision = '770211ecef22'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('papers', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('papers', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
