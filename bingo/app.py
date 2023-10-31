from flask import Flask
from sqlalchemy.orm import DeclarativeBase
from flask_sqlalchemy import SQLAlchemy
from bingo.shell import com
import nltk
from flask_vite import Vite


vite = Vite()

def create_app():
    app = Flask(__name__)

    from bingo.views import main
    app.register_blueprint(main)
    app.register_blueprint(com)

    app.config.from_object('bingo.default_settings')
    app.config.from_envvar('BINGO_SETTINGS', silent=True)

    # language loading
    nltk.download('punkt')
    nltk.download('stopwords')

    vite.init_app(app)

    return app