from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from extensions import db, migrate

# Import your blueprints
from routes import classes_bp, subjects_bp, teachers_bp, school_data_bp, routine_bp
from models import Class, Subject, Teacher, DailyConstraint, TeacherSubject, SchoolData

from environs import Env

env = Env()
env.read_env()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = env.str("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = env.bool(
        "SQLALCHEMY_TRACK_MODIFICATIONS"
    )

    db.init_app(app)
    migrate.init_app(app, db)

    # Register your blueprints
    app.register_blueprint(classes_bp)  # Register classes blueprint
    app.register_blueprint(subjects_bp)  # Register subjects blueprint
    app.register_blueprint(teachers_bp)  # Register teachers blueprint
    app.register_blueprint(school_data_bp)  # Register school data blueprint
    app.register_blueprint(routine_bp)  # Register school data blueprint

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
