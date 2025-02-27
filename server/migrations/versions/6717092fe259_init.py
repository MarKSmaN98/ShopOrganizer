"""init

Revision ID: 6717092fe259
Revises: 
Create Date: 2024-07-30 22:10:08.540369

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6717092fe259'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('techs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('rate', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cars',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('inDate', sa.DateTime(), nullable=True),
    sa.Column('year', sa.Integer(), nullable=True),
    sa.Column('make', sa.String(), nullable=True),
    sa.Column('model', sa.String(), nullable=True),
    sa.Column('owner', sa.String(), nullable=True),
    sa.Column('stage', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['tech_id'], ['techs.id'], name=op.f('fk_cars_tech_id_techs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('images',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], name=op.f('fk_images_car_id_cars')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.Column('tech_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], name=op.f('fk_notes_car_id_cars')),
    sa.ForeignKeyConstraint(['tech_id'], ['techs.id'], name=op.f('fk_notes_tech_id_techs')),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('parts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('hours', sa.Float(), nullable=True),
    sa.Column('car_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['car_id'], ['cars.id'], name=op.f('fk_parts_car_id_cars')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('parts')
    op.drop_table('notes')
    op.drop_table('images')
    op.drop_table('cars')
    op.drop_table('techs')
    # ### end Alembic commands ###
