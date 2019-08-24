from flask import Flask
from app.models.book import db

# 注册app
def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.setting')
    app.config.from_object('app.config.secure')

    # 加载蓝图
    register_blueprint(app)

    # sql
    db.init_app(app)
    db.create_all(app=app)

    return app


# 注册蓝图
def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)
