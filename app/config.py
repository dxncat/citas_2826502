from os import path
basedir = path.abspath(path.dirname(__file__))

class Config:
    # SQLALCHEMY_DATABASE_URI="mysql+pymysql://root:@localhost/citas_2826502"
    SQLALCHEMY_DATABASE_URI="sqlite:///" + path.join(basedir, 'database.db')
    SQLALCHEMY_TRACK_NOTIFICATIONS=True