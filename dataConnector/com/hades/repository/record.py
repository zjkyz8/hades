__author__ = 'xinhuang'

from __init__ import *

db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'xxxxxxxx',
    'db': 'test',
    'charset': 'utf8'
}

engine = create_engine('mysql://%s:%s@%s/%s?charset=%s' % (db_config['user'],
                                                           db_config['passwd'],
                                                           db_config['host'],
                                                           db_config['db'],
                                                           db_config['charset']), echo=True)
metadata = MetaData()
users_table = Table('records', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('name', String(50)),
                    Column('fullname', String(50)),
                    Column('password', String(100))
)
metadata.create_all(engine)

metadata = MetaData(engine)