"""created new tables

Revision ID: 38bfc81797ca
Revises: bbe241934a9b
Create Date: 2020-05-09 16:29:46.473168

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '38bfc81797ca'
down_revision = 'bbe241934a9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('writters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=30), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.Integer(), nullable=True),
    sa.Column('profile_pic_path', sa.String(), nullable=True),
    sa.Column('bio', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('blogs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog', sa.String(), nullable=False),
    sa.Column('posted_date', sa.DateTime(), nullable=True),
    sa.Column('upvotes', sa.Integer(), nullable=True),
    sa.Column('writter_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['writter_id'], ['writters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blogs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['regular_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_unique_constraint(None, 'regular_user', ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'regular_user', type_='unique')
    op.drop_table('comments')
    op.drop_table('blogs')
    op.drop_table('writters')
    # ### end Alembic commands ###
