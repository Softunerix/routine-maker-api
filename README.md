# Routine Maker API

This project uses **Flask**, **PostgreSQL**, and **Google OR-Tools** to generate school routines that respect real-world constraints — specifically tailored for schools following the NCTB (Bangladesh) curriculum..

Run the project by : 

```bash
flask run
```

Before that, you must update the .env and alembic.ini's configuration, and generate migration and upgrade them to PostgreSQL.

```bash
flask db migrate
flask db upgrade
```

# Key Features 

- Fully RESTful API. ([Postman/Insomnia export](https://github.com/Softunerix/routine-maker-api/tree/main/static/insomnia-export.json) is available for quick testing.)
- PostgreSQL Integration: Stores data related to schools, teachers, classes, and subjects.
- Constraint-Driven Scheduling: OR-Tools ensures the routine respects logical and resource-based constraints.
- Modular Codebase: Separated concerns for models, routes, and extensions for clean and scalable development.
- Migration Ready: Uses Flask-Migrate for seamless database migrations.
- Flexible Data Input: Easily add or update teachers, classes, subjects, and shifts via API endpoints.
- Conflict-Free Routines: Ensures schedules are generated without overlapping teachers or repeated subjects.

## Constraints Planning and Schedule Rules

These are the rules the scheduling system follows using OR-Tools:

 - No Teacher Clashes: A teacher can’t be assigned to two classes at the same time.

 - Qualified Teacher Only: Only teachers qualified for a specific class and subject can be assigned.

 - Teacher Availability: Teachers are only scheduled during their available shifts and days.

 - No Subject Repetition: A subject can't be repeated for the same class in a single day.

 - Class Shift Availability: Scheduling checks if the class is active during the specific shift (e.g., morning, afternoon).

 - Subject Coverage: Subjects are assigned the exact required number of sessions per week.


# Limitations 

- No way to handle if a teacher doesn't take any classes on a particular day.
- Not quite dynamic to handle any kind of schools routine generation.
- No way to provide gap between classes for any specific teacher

# Potential Improvements 

Compared to the [previous version](https://github.com/Softunerix/routine-maker/tree/main/schedules), this project generates only one schedule per run, and the resulting CSV is simpler.

- Add shift start/end times in the database and show actual times instead of numeric slots.

- Allow users to customize active days instead of [auto-starting from Saturday](https://github.com/Softunerix/routine-maker-api/blob/main/routine_constraints/generate_routine.py#L28).

- Improve CSV formatting to reflect full teacher-class-subject-time metadata.

- Add schedule visualization (web dashboard or calendar-style output).

- Generate multiple valid schedules and allow user to choose.
