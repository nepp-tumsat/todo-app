import os

class DevelopmentConfig:

    # Flask
    DEBUG = True

    # SQLAlchemy -> dbファイルをおく場所
    SQLALCHEMY_DATABASE_URI = '{dialect}+{driver}://{user}:{password}@{host}/{database}?charset={charset_type}'.format(**{
        'dialect': 'mysql',
        'driver': 'pymysql',
        'user': os.getenv('DB_USER', 'root'),
        'password': os.getenv('DB_PASSWORD', 'password'),
        'host': os.getenv('DB_HOST', '172.30.0.4'),
        'database': os.getenv('DB_DATABASE', 'todo_app'),
        'charset_type': 'utf8'

    })
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True # TrueでSQLが標準出力される



Config = DevelopmentConfig