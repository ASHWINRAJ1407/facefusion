# models.py
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class EngagementResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    engagement_percentage = db.Column(db.Float, nullable=False)
    not_engaged_percentage = db.Column(db.Float, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
