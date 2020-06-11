import json

from flask import request

from api.services.appointments_manager import AppointmentManager
from api.dal.providers_dal import ProvidersDal
from api.vim_api import app


@app.route("/appointments", methods=['GET', 'OPTIONS'])
def get_appointments():
    date = request.args.get('date')
    min_score = request.args.get('minScore')
    specialty = request.args.get('specialty') if request.args.get('specialty') else None

    try:
        date = int(date)
        min_score = float(min_score)
        specialty = specialty.lower()
    except Exception as e:
        return json.dumps({'success': False}), 400

    providers_dal = ProvidersDal()
    provider_names = providers_dal.get_available_providers(specialty, date, min_score)
    return json.dumps(provider_names), 200


@app.route("/appointments", methods=['POST', 'OPTIONS'])
def set_appointment():
    params = request.json
    name = params.get('name')
    date = params.get('date')

    if any(param is None for param in [name, date]):
        return json.dumps({'success': False}), 400

    appointments_manager = AppointmentManager()
    is_valid_appointment = appointments_manager.set_appointment(name, date)

    if is_valid_appointment:
        return json.dumps({'success': True}), 200

    return json.dumps({'success': False}), 400
