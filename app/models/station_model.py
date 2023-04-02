from app.utils.db import db
import datetime

class StationData(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float(5))
    humidity    = db.Column(db.Float(5))
    created_at  = db.Column(db.DateTime, default=datetime.datetime.now)

    def __init__(self, temperature, humidity):
        self.temperature = temperature
        self.humidity = humidity
