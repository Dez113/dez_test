from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

import sys

db = SQLAlchemy()

app = Flask(__name__)
app.config.from_object('alembic_test.config')

# migrate = Migrate(app, db)
db.init_app(app)


from alembic_test import views, models
