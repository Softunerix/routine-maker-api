from ortools.sat.python import cp_model


def build_constraints_and_solve(teachers, classes, num_days, num_shifts):
    model = cp_model.CpModel()

    schedule = {}
    for teacher_name, info_teacher in teachers.items():
        for clss, info_class in classes.items():
            for subject in info_class["subjects"]:
                if subject in info_teacher["classes"].get(
                    clss, []
                ):  # Ensuring the teacher is qualified to teach the subject
                    for day in range(num_days):
                        start_shift = (
                            int(info_teacher["daily_constraints"][day][0]) - 1
                        )  # converting 1-based to 0-based
                        end_shift = int(info_teacher["daily_constraints"][day][1]) - 1

                        for shift in range(start_shift, end_shift + 1):
                            if (
                                (info_class["shift_availability"][day][0] - 1)
                                <= shift
                                <= info_class["shift_availability"][day][1]
                            ):  # making sure shift is valid for that day
                                schedule[(teacher_name, clss, subject, day, shift)] = (
                                    model.NewBoolVar(
                                        f"{teacher_name}_{clss}_{subject}_{day}_{shift}"
                                    )
                                )

    for teacher_name, info_teacher in teachers.items():
        for clss, info_class in classes.items():
            for subject, required_days in info_class["subjects"].items():
                if subject in teachers[teacher_name]["classes"].get(
                    clss, []
                ):  # Ensuring the teacher is qualified to teach the subject
                    # Sum of all shifts across all days for this subject must equal the required days

                    # ----------------1st constraint--------------
                    model.Add(
                        sum(
                            schedule[(teacher_name, clss, subject, day, shift)]
                            for day in range(
                                num_days
                            )  # iterate over the days to assign the subject for the required number of days
                            for shift in range(
                                int(info_teacher["daily_constraints"][day][0]) - 1,
                                int(info_teacher["daily_constraints"][day][1]),
                            )  # iterating over the shifts when the teacher is available
                            if (
                                (info_class["shift_availability"][day][0] - 1)
                                <= shift
                                <= info_class["shift_availability"][day][1]
                            )  # checking if the class is available at that if
                        )
                        == required_days
                    )

    for clss, info_class in classes.items():
        for day in range(num_days):
            for shift in range(num_shifts[day]):
                # ----------------3rd constraint--------------
                model.Add(
                    sum(
                        schedule.get((teacher_name, clss, subject, day, shift), 0)
                        for teacher_name, info_teacher in teachers.items()
                        for subject, required_days in info_class["subjects"].items()
                    )
                    <= 1
                )  # multiple teacher can't teach a class in the same shift simultaneously

    for clss, info_class in classes.items():
        for day in range(num_days):
            for subject, required_days in info_class["subjects"].items():
                # ----------------4th constraint--------------
                model.Add(
                    sum(
                        schedule.get((teacher_name, clss, subject, day, shift), 0)
                        for teacher_name, info_teacher in teachers.items()
                        for shift in range(num_shifts[day])
                    )
                    <= 1
                )  # can't teach the same subject multiple times a day

    solver = cp_model.CpSolver()
    status = solver.Solve(model)

    return schedule, solver, status, teachers
    # if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    #     for teacher in teachers:
    #         print(f"\nSchedule for {teacher}:")
    #         for key, value_var in schedule.items():  # Iterate through schedule items
    #             if solver.Value(value_var) == 1:
    #                 t, cls, subject, day, shift = key
    #                 if t == teacher:  # Filter for the current teacher
    #                     print(f"  Day {day}, Shift {shift}: {cls} - {subject}")
    # else:
    #     print("No solution found!")
