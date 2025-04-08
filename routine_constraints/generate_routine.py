import io
import csv
import zipfile

from .constraints import build_constraints_and_solve
from ortools.sat.python import cp_model


def routine_generation(teachers, classes, num_days, num_shifts):
    schedule, solver, status, teachers = build_constraints_and_solve(
        teachers, classes, num_days, num_shifts
    )
    if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
        results = []
        for teacher in teachers:
            print(f"\nSchedule for {teacher}:")
            for key, value_var in schedule.items():  # Iterate through schedule items
                if solver.Value(value_var) == 1:
                    t, cls, subject, day, shift = key
                    results.append((t, cls, subject, day, shift))

        results.sort(key=lambda x: (x[0], x[3], x[4]))  # teacher, then day, then shift

        # 5) Generate CSV in memory
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["Teacher", "Class", "Subject", "Day", "Shift"])

        # If you want day names:
        day_names = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
        for teacher_name, cls_name, subject, day, shift in results:
            # +1 if you want to show shift # as 1-based
            writer.writerow(
                [
                    teacher_name,
                    cls_name,
                    subject,
                    day_names[day] if day < len(day_names) else f"Day {day + 1}",
                    shift + 1,
                ]
            )

        # Move to start of StringIO
        output.seek(0)

        # 6) Return as downloadable CSV
        return output
    else:
        print("No solution found!")
