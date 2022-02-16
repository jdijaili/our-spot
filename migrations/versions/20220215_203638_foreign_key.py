"""foreign key

Revision ID: 8d34b315633f
Revises: c61813287146
Create Date: 2022-02-15 20:36:38.855470

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d34b315633f'
down_revision = 'c61813287146'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'comments', 'parks', ['park_id'], ['id'])
    op.create_foreign_key(None, 'comments', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'favorites', 'parks', ['park_id'], ['id'])
    op.create_foreign_key(None, 'favorites', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'lists', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'park_list_joins', 'users', ['list_id'], ['id'])
    op.create_foreign_key(None, 'park_list_joins', 'parks', ['park_id'], ['id'])
    op.create_foreign_key(None, 'park_photos', 'users', ['user_id'], ['id'])
    op.create_foreign_key(None, 'park_photos', 'parks', ['park_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'park_photos', type_='foreignkey')
    op.drop_constraint(None, 'park_photos', type_='foreignkey')
    op.drop_constraint(None, 'park_list_joins', type_='foreignkey')
    op.drop_constraint(None, 'park_list_joins', type_='foreignkey')
    op.drop_constraint(None, 'lists', type_='foreignkey')
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.drop_constraint(None, 'favorites', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    op.drop_constraint(None, 'comments', type_='foreignkey')
    # ### end Alembic commands ###
