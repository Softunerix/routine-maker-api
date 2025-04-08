from sqlalchemy.dialects.postgresql import ARRAY
from extensions import db


class Class(db.Model):
    __tablename__ = "classes"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True)
    shift_availability = db.Column(ARRAY(db.Integer))

    def __repr__(self):
        return f"<Class {self.name}>"
