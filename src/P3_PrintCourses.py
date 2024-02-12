# Class generates a list of schedules
# Tony Situ 
# 2023-06-15

from P2_GenerateSchedules import create_schedules
from datetime import time, timedelta
import pickle
import os


def __get_schedules() -> list:
    """
    Returns a list of 3 generated schedules from the top of the max heap
    """
    schedules, *_ = create_schedules()
    schedule1, schedule2, schedule3 = schedules[0], schedules[1], schedules[2]
    return list((schedule1, schedule2, schedule3))


def __get_schedule_count() -> int:
    """
    Returns the number of schedules the user has generated.
    """
    counter_file = "ScheduleCounter.pkl"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    pkl_dir = os.path.join(data_dir, counter_file)

    try:
        with open(pkl_dir, "rb") as pkl_file:
            schedule_counter = pickle.load(pkl_file)
    except FileNotFoundError:
        with open(pkl_dir, "wb") as pkl_file:
            schedule_counter = 0
            pickle.dump(schedule_counter, pkl_file)
    except (PermissionError, OSError) as e:
        print(f"Error accessing file: {e}")

    return schedule_counter


def print_schedules():
    """
    Creates a txt file that contains the schedules in a table
    """
    schedule_count = __get_schedule_count()
    string = ""
    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
    schedules = __get_schedules()
    for index in range(3):
        string += "{0: ^7}|".format("Time")
        for day_of_week in weekdays:
            string += "{0: ^21}|".format(day_of_week)

        string += "\n" + "-" * 119

        for timing in range(8, 21):
            for increment_time in range(0, 60, 30):
                time_block = time(timing, increment_time)
                string += "\n\n" + "{0: ^7}|".format(time_block.strftime('%H:%M'))
                for weekday in weekdays:
                    found_course = False
                    for course in schedules[index].get_course_list():
                        if ((course.get_start_time() - timedelta(
                                minutes=5)).time() <= time_block <= course.get_end_time().time() and
                                weekday in course.get_days()):
                            string += "{0: ^21}|".format(course.get_code() + course.get_section())
                            found_course = True

                    if found_course is False:
                        string += "{0: ^21}|".format("")

        string += f"\n\n{schedules[index]}\n"
        string += "Course Codes: {}\n".format(", ".join("{}{}".format(
            code, section) for code, section in
                   zip(schedules[index].get_code_list(), schedules[index].get_section_list())))

        string += "Crn List: {}\n\n".format(", ".join(str(crn) for crn in schedules[index].get_crn()))
        print(string, end="")

    schedule_count += 1
    output_file = "Schedule_" + str(schedule_count) + ".txt"
    print(output_file)
    counter_file = "ScheduleCounter.pkl"
    current_dir = os.path.dirname(os.path.realpath(__file__))
    data_dir = os.path.join(current_dir, "..", "data")
    pkl_dir = os.path.join(data_dir, counter_file)

    with open(pkl_dir, "wb") as file:
        pickle.dump(schedule_count, file)

    generated_schedules_dir = os.path.join(current_dir, "..", "GeneratedSchedules")
    output_file_dir = os.path.join(generated_schedules_dir, output_file)
    with open(output_file_dir, "w") as output_file:
        output_file.write(string)


def main():
    print_schedules()


if __name__ == "__main__":
    main()
