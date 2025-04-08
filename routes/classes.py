from flask import Blueprint, request, jsonify
from models import Class
from extensions import db

# Create a Blueprint for this section of routes
classes_bp = Blueprint("classes", __name__)


# Route to get all classes
@classes_bp.route("/class", methods=["GET"])
def get_classes():
    classes = Class.query.all()
    return jsonify(
        [
            {
                "id": cls.id,
                "name": cls.name,
                "shift_availability": cls.shift_availability,
            }
            for cls in classes
        ]
    )


# Route to create a new class
@classes_bp.route("/class", methods=["POST"])
def add_class():
    data = request.get_json()
    new_class = Class(name=data["name"], shift_availability=data["shift_availability"])
    db.session.add(new_class)
    db.session.commit()
    return jsonify({"message": "Class created successfully"}), 201
