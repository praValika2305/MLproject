"""Initial migration

Revision ID: 37b333669c2c
Revises: 
Create Date: 2024-08-10 11:49:14.937058

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '37b333669c2c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('movie',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('genres', sa.String(), nullable=False),
    sa.Column('imdb_id', sa.Integer(), nullable=True),
    sa.Column('tmdb_id', sa.Integer(), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('release_date', sa.String(), nullable=True),
    sa.Column('poster_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('movielens_movies',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('movie_name', sa.String(), nullable=False),
    sa.Column('genres', sa.String(), nullable=False),
    sa.Column('tmdb_id', sa.Integer(), nullable=True),
    sa.Column('imdb_id', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('movie_id')
    )
    op.create_table('movielens_ratings',
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('movielens_user_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('movie_id', 'movielens_user_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('occupation', sa.String(), nullable=True),
    sa.Column('preferred_genre', sa.String(), nullable=True),
    sa.Column('recommended_genre', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('firebase_uid', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('firebase_uid'),
    sa.UniqueConstraint('username')
    )
    op.create_table('user_ratings',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    op.create_table('user_reviews',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.Column('review', sa.Text(), nullable=True),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_watched',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    op.create_table('user_watchlist',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('movie_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['movie_id'], ['movie.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'movie_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_watchlist')
    op.drop_table('user_watched')
    op.drop_table('user_reviews')
    op.drop_table('user_ratings')
    op.drop_table('user')
    op.drop_table('movielens_ratings')
    op.drop_table('movielens_movies')
    op.drop_table('movie')
    op.drop_table('genre')
    # ### end Alembic commands ###
