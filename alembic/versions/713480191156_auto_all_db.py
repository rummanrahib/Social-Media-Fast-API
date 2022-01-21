"""auto all db

Revision ID: 713480191156
Revises: 4a4a7f9a988f
Create Date: 2022-01-21 22:35:58.213054

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '713480191156'
down_revision = '4a4a7f9a988f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('likes',
    sa.Column('userId', sa.Integer(), nullable=False),
    sa.Column('postId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['postId'], ['posts.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('userId', 'postId')
    )
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    op.add_column('posts', sa.Column('published', sa.Boolean(), server_default='TRUE', nullable=False))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False))
    op.add_column('posts', sa.Column('userId', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'posts', 'users', ['userId'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'userId')
    op.drop_column('posts', 'created_at')
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'content')
    op.drop_table('likes')
    op.drop_table('users')
    # ### end Alembic commands ###