import os

basedir = os.path.abspath(os.path.dirname(__file__))
#db_path = os.path.join(basedir, '../data-dev.sqlite')

DEBUG = True
IGNORE_AUTH = True
SECRET_KEY = 'top-secret!'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:farzin@localhost/presentDb'