from flask import Blueprint, request, jsonify
from models import SchoolData, Class
from extensions import db

school_data_bp = Blueprint('school_data', __name__)

# Route to get school data for a specific class
@school_data_bp.route('/school_data', methods=['GET'])
def get_school_data():
    school_data = SchoolData.query.first()
    if school_data:
        return jsonify({'num_days': school_data.num_days,'num_shifts': school_data.num_shifts})
    else:
        return jsonify({'message': 'School data not found for this class'}), 404

# Route to add school data for a class
@school_data_bp.route('/school_data', methods=['POST'])
def add_school_data():
    data = request.get_json()
    new_school_data = SchoolData(num_days=data['num_days'], num_shifts=data['num_shifts'])
    db.session.add(new_school_data)
    db.session.commit()
    return jsonify({'message': 'School data created successfully'}), 201
