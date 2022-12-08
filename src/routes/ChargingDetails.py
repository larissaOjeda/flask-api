from flask import Blueprint, jsonify, request
import uuid

# Entities 
from models.entities.ChargingDetails import ChargingDetails 

# Models
from models.ChargingDetailsModel import ChargingDetailsModel
from models.StatisticsModel import StatisticsModel

# Utils 
from utils.VinValidation import VinValidation

main = Blueprint('charging_detail_blueprint', __name__)

@main.route('/')
def get_all(): 
    try:
        chargingDetails = ChargingDetailsModel.get_all()
        return jsonify(chargingDetails)
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500


@main.route('/create', methods=['POST'])
def create_charging_detail():
    try:
        vin = request.json['vin']
        if not VinValidation.is_vin_valid(vin):
            return jsonify({'message' : "Invalid Vin"}), 401
        id = str(uuid.uuid4())
        chargingDetail = ChargingDetails(str(vin), id)
        
        affected_rows = ChargingDetailsModel.create_charging_detail(chargingDetail)

        if affected_rows == 1: 
            return jsonify(chargingDetail.id), 201
        else:
            return jsonify({'message' : "Error creating chargingDetail"}), 500
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500

@main.route('/update/<id>', methods=['PUT'])
def update_charging_detail(id):
    try:
        record = ChargingDetailsModel.get_by_id(id)
        if not record: 
            return jsonify({'message': 'No entity updated'}), 404


        affected_rows = ChargingDetailsModel.update_charging_detail(id)

        if affected_rows == 1:
            return jsonify({}), 204
        
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500

@main.route('/statistics')
def get_statistics(): 
    try:
        stats = StatisticsModel.generate_statistics()
        return stats, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500

@main.route('/plot')
def get_plot(): 
    try:
        plot = StatisticsModel.generate_plot()
        return plot, 200
    except Exception as ex: 
        return jsonify({'message' : str(ex)}), 500