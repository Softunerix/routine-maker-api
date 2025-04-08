from flask import Blueprint, request, jsonify
from models import Subject, Class
from extensions import db

subjects_bp = Blueprint('subjects', __name__)

# Route to get all subjects for a specific class
@subjects_bp.route('/class/<int:class_id>/subjects', methods=['GET'])
def get_subjects_by_class(class_id):
    class_ = Class.query.get_or_404(class_id)
    return jsonify([{'id': subject.id, 'name':subject.name, 'num_days':subject.num_days} for subject in class_.subject_class])

# Route to create a new subject for a class
@subjects_bp.route('/class/<int:class_id>/subject', methods=['POST'])
def add_subject(class_id):
    data = request.get_json()
    class_ = Class.query.get_or_404(class_id)
    new_subject = Subject(num_days=data['num_days'], name=data['name'], class_id=class_.id)
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({'message': 'Subject created successfully'}), 201
