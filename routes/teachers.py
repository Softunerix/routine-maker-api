from flask import Blueprint, request, jsonify
from models import Teacher, DailyConstraint, TeacherSubject
from extensions import db

teachers_bp = Blueprint("teachers", __name__)


# Route to get all teachers
@teachers_bp.route("/teachers", methods=["GET"])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify(
        [
            {
                "id": teacher.id,
                "name": teacher.name,
                "subjects": [
                    {
                        "subject_id": assoc.subject_id,
                        "subject_name": assoc.subject.name if assoc.subject else None,
                    }
                    for assoc in teacher.teacher_subject_associated
                ],
                "constraints": (
                    {
                        "id": teacher.teacher_constraint[0].id,
                        "num_shifts": teacher.teacher_constraint[0].num_shifts,
                    }
                    if teacher.teacher_constraint
                    else None
                ),
            }
            for teacher in teachers
        ]
    )


# Route to add a new teacher
@teachers_bp.route("/teacher", methods=["POST"])
def add_teacher():
    data = request.get_json()
    new_teacher = Teacher(name=data["name"])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Teacher created successfully"}), 201


# Route to add a teacher subject
@teachers_bp.route("/teacher/<int:teacher_id>/subject", methods=["POST"])
def add_subject(teacher_id):
    data = request.get_json()
    add_teachers_subject = TeacherSubject(
        teacher_id=teacher_id, subject_id=data["subject_id"]
    )
    db.session.add(add_teachers_subject)
    db.session.commit()
    return jsonify({"message": "The teacher's subject created successfully"}), 201


# Route to add a teacher constraint
@teachers_bp.route("/teacher/<int:teacher_id>/constraint", methods=["POST"])
def add_constraint(teacher_id):
    data = request.get_json()
    daily_constraint = DailyConstraint(
        teacher_id=teacher_id, num_shifts=data["num_shifts"]
    )
    db.session.add(daily_constraint)
    db.session.commit()
    return (
        jsonify(
            {"message": "Daily Constraint for the teacher is created successfully"}
        ),
        201,
    )
