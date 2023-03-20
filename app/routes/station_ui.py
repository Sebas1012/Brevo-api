from flask import Blueprint, render_template

station_ui = Blueprint('station_ui', __name__)

@station_ui.route('/')
def ui():
    return render_template('station.html')