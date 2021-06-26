from alembic_test import db
from sqlalchemy.dialects.postgresql import JSON


class Logs(db.Model):
    """
    Logs that stored in db
    """
    __tablename__ = 'logs'

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    message = db.Column(JSON)
    valid = db.Column(db.Boolean)

