"""empty message

Revision ID: 7b1ea527e4c7
Revises: 
Create Date: 2023-11-08 12:13:07.888563

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7b1ea527e4c7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('Search_table',
    sa.Column('XH', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('MC', sa.String(length=200), nullable=False),
    sa.Column('MCJX', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('XH')
    )
    op.drop_table('豆瓣电影采集爬虫2023_11_2')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('豆瓣电影采集爬虫2023_11_2',
    sa.Column('电影名', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('电影id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('年代', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('时光评分', mysql.DOUBLE(asdecimal=True), nullable=True),
    sa.Column('评论人数', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('导演', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('编剧', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('类型', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('国家地区', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('发行公司', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('片长', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('上映日期', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('剧情介绍', mysql.VARCHAR(length=255), nullable=True),
    sa.Column('主演', mysql.VARCHAR(length=255), nullable=True),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('Search_table')
    # ### end Alembic commands ###
