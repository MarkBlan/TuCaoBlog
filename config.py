import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    #TODO:
    SECRET_KEY = 'SECRET_KEY'
    #SECRET_KEY = os.environ.get('SECRET_KEY')
    #邮件设置
    MAIL_SERVER = 'smtp.126.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    #TODO: IF PRODUCTION
    #MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_USERNAME = 'ZQ50314@126.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_SUPPRESS_SEND = False
    DARKWEBCHINA_MAIL_SUBJECT_PREFIX = '[DarkWebChina]'
    DARKWEBCHINA_MAIL_SENDER = 'ZQ050314@126.com'
    DARKWEBCHINA_ADMIN = os.environ.get('DARKWEBCHINA_ADMIN')
    DARKWEBCHINA_POSTS_PER_PAGE = 20
    #数据库设置，如需设置，请取消'#'符合
    #数据库设置如果设置成 True (默认情况)
    # Flask-SQLAlchemy 将会追踪对象的修改并且发送信号
    # 这需要额外的内存， 如果不必要的可以禁用它
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    DARKWEBCHINA_FOLLOWERS_PER_PAGE = 50

    #sqlite:////tmp/test.db
    #mysql://username:password@server/db#
    #postgresql://scott:tiger@localhost/mydatabase
    #oracle://scott:tiger@127.0.0.1:1521/sidname
    #SQLALCHEMY_DATABASE_URI---在不同环境下设置
    #如果设置成 True，SQLAlchemy 将会记录所有 发到标准输出(stderr)的语句，这对调试很有帮助
    #SQLALCHEMY_ECHO
    #可以用于显式地禁用或者启用查询记录。查询记录 在调试或者测试模式下自动启用
    #SQLALCHEMY_RECORD_QUERIES
    #可以用于显式地禁用支持原生的 unicode。这是 某些数据库适配器必须的
    #SQLALCHEMY_NATIVE_UNICODE
    #数据库连接池的大小。默认是数据库引擎的默认值 （通常是 5）
    #SQLALCHEMY_POOL_SIZE
    #指定数据库连接池的超时时间。默认是 10。
    #SQLALCHEMY_POOL_TIMEOUT
    #自动回收连接的秒数。这对 MySQL 是必须的，
    #默认 情况下 MySQL 会自动移除闲置 8 小时或者以上的连接。
    #需要注意地是如果使用 MySQL 的话， Flask-SQLAlchemy 会自动地设置这个值为 2 小时。
    #SQLALCHEMY_POOL_RECYCLE
    #控制在连接池达到最大值后可以创建的连接数。当这些额外的 连接回收到连接池后将会被断开和抛弃。
    #SQLALCHEMY_MAX_OVERFLOW

    @staticmethod
    def init_app(app):
        pass

#'sqlite:////home/flask/flasky/data.sqlite'
#开发环境数据库路径
class DevelopmentConfig(Config): 
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_dev.sqlite') 
    #SQLALCHEMY_DATABASE_URL = os.environ.get('DEV_DATABASE_URL')

#测试环境数据库路径
class TestingConfig(Config):
    TESTING = True
    #SQLALCHEMY_DATABASE_URL =  os.environ.get('DEV_DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data_test.sqlite') 

#生产环境数据库路径
class ProductionConfig(Config):
    #SQLALCHEMY_DATABASE_URL =  os.environ.get('DATABASE_URL')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite') 


config = {
    'development': DevelopmentConfig,
    'testing':TestingConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig
}



