from flask import Blueprint, Response, jsonify
from routine_constraints import routine_generation
from models import Class, Subject, Teacher, DailyConstraint, TeacherSubject, SchoolData

# Create a Blueprint for this section of routes
routine_bp = Blueprint("routine", __name__)


# Route to get all routine
@routine_bp.route("/routine", methods=["GET"])
def get_routine():
    teachers_dict, classes_dict, num_days, num_shifts = build_scheduling_data()

    file = routine_generation(teachers_dict, classes_dict, num_days, num_shifts)
    # if file != False:
    #     return jsonify({"message": "No feasible solution found"}), 404

    return Response(
        file,
        mimetype="text/csv",
        headers={"Content-Disposition": "attachment;filename=routine.csv"},
    )


def build_scheduling_data():
    school_data = SchoolData.query.first()
    if not school_data:
        raise ValueError("No row found in SchoolData table!")

    num_days = school_data.num_days  # e.g. 6
    num_shifts = school_data.num_shifts  # e.g. [3,3,3,3,3,3]

    # 2) Build the `classes` dict
    #    classes = {
    #       "class1": {
    #         "subjects": {"Math": 6, "English": 6, ...},
    #         "shift_availability": [ [1,3], [1,3], [1,3], ...]
    #       },
    #       ...
    #    }
    classes_dict = {}
    all_classes = Class.query.all()

    for c in all_classes:
        # c.shift_availability might be a 2D array or a list of "1-3" strings; adapt as needed
        raw_shifts = c.shift_availability or []
        # Example parse if it's an array of "start-end" strings:
        shift_availability = []
        for shift_str in raw_shifts:  # e.g. "1-3"
            if isinstance(shift_str, str) and "-" in shift_str:
                start_str, end_str = shift_str.split("-")
                shift_availability.append([int(start_str), int(end_str)])
            else:
                # If it's already [1,3], just append
                shift_availability.append(shift_str)

        # Gather subjects for this class
        # Relationship: each Subject has class_id = c.id
        # Or if you have a relationship set up, you could do c.subject_class
        subjects = Subject.query.filter_by(class_id=c.id).all()

        # Build a dict like {"Math": 6, "Bengali": 6, ...}
        subjects_map = {}
        for subj in subjects:
            subjects_map[subj.name] = subj.num_days  # or subj.required_hours

        classes_dict[c.name] = {
            "subjects": subjects_map,
            "shift_availability": shift_availability,
        }

    teachers_dict = {}
    all_teachers = Teacher.query.all()

    for t in all_teachers:
        # (a) daily constraints
        daily_constraints_list = []
        # teacher_constraint is the backref from DailyConstraint to Teacher
        # If you declared: backref=db.backref("teacher_constraint", lazy=True)
        # then t.teacher_constraint is a list
        # but you used `unique=True` on teacher_id, so presumably there's exactly 1 row. Let's get it:
        constraint_row = DailyConstraint.query.filter_by(teacher_id=t.id).first()
        if constraint_row and constraint_row.num_shifts:
            for shift_str in constraint_row.num_shifts:
                if isinstance(shift_str, str) and "-" in shift_str:
                    start_str, end_str = shift_str.split("-")
                    daily_constraints_list.append([int(start_str), int(end_str)])
                else:
                    # If it's already [1,3], etc.
                    daily_constraints_list.append(shift_str)

        # (b) Classes + subjects teacher can teach
        # teacher_subject_associated is the backref from TeacherSubject
        # We can see which (Subject) objects they link to, and from Subject we can see which Class it belongs to
        class_subj_map = (
            {}
        )  # e.g. {"class1": set(["English","Bengali"]), "class2": set(["H. Math"])}

        teacher_subject_links = TeacherSubject.query.filter_by(teacher_id=t.id).all()
        for link in teacher_subject_links:
            subj_obj = link.subject  # the Subject
            if not subj_obj:
                continue

            class_obj = subj_obj.class_  # the Class via subject.class_
            if not class_obj:
                continue

            class_name = class_obj.name
            if class_name not in class_subj_map:
                class_subj_map[class_name] = set()

            class_subj_map[class_name].add(subj_obj.name)

        teachers_dict[t.name] = {
            "classes": class_subj_map,
            "daily_constraints": daily_constraints_list,
        }

    return teachers_dict, classes_dict, num_days, num_shifts
