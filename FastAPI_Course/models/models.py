from sqlalchemy import Table, Column, MetaData, Integer, String, TIMESTAMP, ForeignKey, JSON
from datetime import datetime

metadata = MetaData()


roles = Table(
    'roles',
    metadata,
    Column('id', primary_key=True),
    Column('name', String, nullable=False),
    Column('permission', JSON),
)


users = Table(
    'users',
    metadata,
    Column('id', primary_key=True),
    Column('email', nullable=False),
    Column('username', String, nullable=False),
    Column('password', String, nullable=False),
    Column('created_at', TIMESTAMP, default=datetime.utcnow),
    Column('role_id', Integer, ForeignKey('roles.id'))
)
