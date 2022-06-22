from flask import Flask
from flaskr.extensions import db
from flaskr.routes import main
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:savpostgres@localhost:5432/bloom_app"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(main)

    return app
