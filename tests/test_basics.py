import unittest
#载入当前应用
from flask import current_app
#载入创建应用，数据库实例
from app import create_app, db

class BasicsTestCase(unittest.TestCase):
    def setUp(self):
        #载入配置是testing的配置数据库
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exists(self):
        self.assertFalse(current_app is None)

    def test_app_is_testing(self):
        self.assertTrue(current_app.config['TESTING'])
