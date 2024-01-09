# yacut/yacut/models.py

from datetime import datetime

from yacut import db


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(2000), nullable=False)
    short = db.Column(db.String(6), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
