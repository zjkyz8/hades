__author__ = 'xinhuang'

from __init__ import *

class BaseMapper:
    def __init__(self):
        app = Flask(__name__)
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:d@localhost/hades'
        app.config['SQLALCHEMY_ECHO'] = True
        self.db = SQLAlchemy(app)