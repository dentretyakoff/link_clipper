# yacut/yacut/models.py

from datetime import datetime

from yacut import db
from settings import MAX_LEN_ORIGINAL, MAX_LEN_SHORT


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_LEN_ORIGINAL), nullable=False)
    short = db.Column(db.String(MAX_LEN_SHORT), nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
