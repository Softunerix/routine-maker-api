from sqlalchemy.dialects.postgresql import ARRAY
from extensions import db


class Teacher(db.Model):
    __tablename__ = "teachers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    def __repr__(self):
        return f"<Teacher {self.name}>"


class DailyConstraint(db.Model):
    __tablename__ = "teacher_daily_constraint"
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"), unique=True)
    num_shifts = db.Column(ARRAY(db.Integer))

    teacher = db.relationship(
        "Teacher", backref=db.backref("teacher_constraint", lazy=True)
    )

    def __repr__(self):
        return f"<DailyConstraint {self.name}>"

    def validate_num_shifts(self):
        """
        Validates that the number of shifts matches the number of days from the school_data table.
        Ensures that the shifts are in the correct format ("1-6", "2-5", etc.).
        """
        # Fetch the num_days for the class from the school_data table
        num_days = self.school_data[0].num_days if self.school_data else 0

        if len(self.num_shifts) != num_days:
            raise ValueError(
                f"The number of shifts ({len(self.num_shifts)}) must match the number of days ({num_days}) in the school data."
            )

        for shift in self.num_shifts:
            # Validate the shift format (e.g., "1-6", "2-5", etc.)
            if not isinstance(shift, str) or "-" not in shift:
                raise ValueError(
                    f"Invalid shift format: {shift}. Expected format 'start-end'."
                )
            start, end = shift.split("-")
            if not start.isdigit() or not end.isdigit():
                raise ValueError(
                    f"Invalid shift range: {shift}. Both start and end should be numbers."
                )
            if int(start) > int(end):
                raise ValueError(
                    f"Invalid shift range: {shift}. Start period must be less than or equal to end period."
                )


class TeacherSubject(db.Model):
    __tablename__ = "teacher_subject"
    id = db.Column(db.Integer, primary_key=True)
    teacher_id = db.Column(db.Integer, db.ForeignKey("teachers.id"))
    subject_id = db.Column(db.Integer, db.ForeignKey("subjects.id"))

    teacher = db.relationship(
        "Teacher", backref=db.backref("teacher_subject_associated", lazy=True)
    )
    subject = db.relationship(
        "Subject", backref=db.backref("teacher_subject", lazy=True)
    )

    def __repr__(self):
        return f"<TeacherSubject {self.name}>"
