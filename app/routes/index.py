from flask import Blueprint, redirect

index = Blueprint('index', __name__)

@index.route('/')
def change():
    return redirect('/api/v1/station/data')