from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask_pagedown import PageDown



#登录管理
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
#login.login_message = _l('Please log in to access this page.')

#邮箱
mail = Mail()

#使用Twitter模板
bootstrap = Bootstrap()

#网页时间插件
moment = Moment()

pagedown = PageDown()

def create_app(config_name):
    #创建应用
    app = Flask(__name__)
    #载入配置
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    #载入Twitter模板
    bootstrap.init_app(app)
    #载入邮箱配置
    mail.init_app(app)
    #载入网页时间控制
    moment.init_app(app)
    #载入数据库设置
    db.init_app(app)
    #载入登录管理
    login_manager.init_app(app)
    pagedown.init_app(app)

    #主页面蓝图注册
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #登录界面蓝图注册
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app

#DataBase Use
db = SQLAlchemy()