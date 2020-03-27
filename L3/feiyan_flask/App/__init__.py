from flask import Flask

from App.ext import init_ext
from App.views import init_blue

def create_app():

    app = Flask(__name__)
    # 初始化app
    # 配置flask配置对象中键：SQLALCHEMY_DATABASE_URI

    app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://wucai:wucai1234!@rm-uf6z891lon6dxuqblqo.mysql.rds.aliyuncs.com:3306/nba_data"
    #


    # 配置flask配置对象中键：SQLALCHEMY_COMMIT_TEARDOWN,设置为True,应用会自动在每次请求结束后提交数据库中变动
    app.config['SECRET_KEY'] = '123456'
    app.config['SQLALCHEMY_COMMIT_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True


    # 初始化蓝图，路由
    init_blue(app)

    # 初始化第三方库
    init_ext(app)
    return app



