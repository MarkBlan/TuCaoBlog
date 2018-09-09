import os
from flask_migrate import Migrate
from app import create_app,db
from app.models import User,Role,Permission,Post
import click

app = create_app(os.getenv('DARKWEBCHINA_CONFIG'))
migrate = Migrate(app,db)

#装饰器使Flask知道这些shell上下文对象
#每次启动 shell 会话都要导入数据库实例和模型
#为shell 命令注册一个 make_context 回调函数完成这个工作
@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, Role=Role, Permission=Permission, Post=Post)


#flask_cli 代替 flask_scriptrun    
#run Runs a development server.shell  Runs a shell in the app context.
# EXPORT FLASK_APP=flasky.py flask run

#app.cli.command()装饰器提供了接口给Click
@app.cli.command()
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)