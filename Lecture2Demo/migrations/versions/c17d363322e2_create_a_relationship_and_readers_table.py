"""Create a relationship and readers table 

Revision ID: c17d363322e2
Revises: 815f1b664711
Create Date: 2021-11-15 20:00:05.304195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c17d363322e2'
down_revision = '815f1b664711'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('books')
    op.add_column('readers', sa.Column('last_name', sa.String(), nullable=False))
    op.drop_column('readers', 'second_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('readers', sa.Column('second_name', sa.VARCHAR(length=255), autoincrement=False, nullable=False))
    op.drop_column('readers', 'last_name')
    op.create_table('books',
    sa.Column('pk', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('author', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('reader_pk', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['reader_pk'], ['readers.pk'], name='books_reader_pk_fkey'),
    sa.PrimaryKeyConstraint('pk', name='books_pkey')
    )
    # ### end Alembic commands ###
