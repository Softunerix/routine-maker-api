from extensions import db

class Subject(db.Model):
    __tablename__ = 'subjects'
    id = db.Column(db.Integer, primary_key=True)
    class_id = db.Column(db.Integer, db.ForeignKey('classes.id'))
    name = db.Column(db.String(200))
    num_days = db.Column(db.Integer)

    class_ = db.relationship('Class', backref=db.backref('subject_class', lazy=True))

    def __repr__(self):
        return f'<Subject {self.name}>'