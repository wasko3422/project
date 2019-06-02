from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
bootstrap = Bootstrap(app)
login = LoginManager(app)
login.login_view = 'login'

from app import routes, models