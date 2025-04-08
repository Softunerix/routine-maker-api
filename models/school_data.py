from sqlalchemy.dialects.postgresql import ARRAY
from extensions import db

class SchoolData(db.Model):
    __tablename__ = 'school_data'
    id = db.Column(db.Integer, primary_key=True)
    num_days = db.Column(db.Integer)
    num_shifts = db.Column(ARRAY(db.Integer))  # Store num_shifts as an array of integers

    def __repr__(self):
        return f'<SchoolData {self.id}>'
