from flask import Blueprint, jsonify, request
from app.utils.db import db
from app.models.station_model import StationData
from app.schemas.station_schema import StationSchema

station_api = Blueprint('station_api', __name__, url_prefix='/api/v1/station')

@station_api.get('/data')
def get_data():
    station_schema_2 = StationSchema(many=True)
    data = StationData.query.all()
    result = station_schema_2.dump(data)

    return jsonify(result)

@station_api.get('/data/<id>')
def get_id(id):
    station_schema = StationSchema()
    data = StationData.query.get(id)

    return station_schema.jsonify(data)



    
@station_api.post('/data')
def create_data():
    station_schema = StationSchema()

    temperature = request.json['temperature']
    humidity = request.json['humidity']

    data = StationData(temperature, humidity)
    db.session.add(data)
    db.session.commit()

    return station_schema.jsonify(data)

    
