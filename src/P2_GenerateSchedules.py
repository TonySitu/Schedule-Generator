# Class generates a list of schedules
# Tony Situ 
# 2023-06-13

import itertools

from P1_GenerateCourses import create_course_dict
from Schedule import Schedule
from BinaryMaxHeap import BinaryMaxHeap
import os


def create_schedules() -> tuple[BinaryMaxHeap, int]:
    schedule_heap = BinaryMaxHeap()
    course_dict = create_course_dict()
    schedule_counter = 0
    current_dir = os.path.dirname(os.path.realpath(__file__))
    user_data_dir = os.path.join(current_dir, "..", "UserData")
    criteria_dir = os.path.join(user_data_dir, "Criteria.txt")

    counter = 0
    with open(criteria_dir) as criteria_file:
        for combinations_of_courses in itertools.product(*course_dict.values()):
            course_schedule_list = list(combinations_of_courses)
            tutorial_schedules = []
            for schedule in course_schedule_list:
                tutorial_schedules.append(schedule.get_tutorials())

            for combinations_of_tutorials in itertools.product(*tutorial_schedules):
                tutorial_schedule_list = list(combinations_of_tutorials)
                final_schedule = Schedule(course_schedule_list + tutorial_schedule_list)

                is_valid = __is_valid_schedule(final_schedule.get_course_list())
                if is_valid:
                    criteria_file.seek(0)
                    final_schedule.rate(criteria_file)
                    schedule_heap.add(final_schedule)
                    schedule_counter += 1

    return schedule_heap, schedule_counter


def __is_valid_schedule(schedule: list) -> bool:
    for index, course in enumerate(schedule):  # iterates through courses in schedule
        for other_course in schedule[index + 1: len(schedule)]:
            if course.has_conflict(other_course):  # checks if schedule has time conflicts
                return False

    return True


def main() -> None:
    schedules, schedule_counter = create_schedules()
    print("----------------------------------------------------------------------")
    for schedule in schedules:
        print(str(schedule) + "\n")

    print("number of schedules", len(schedules))
    print("----------------------------------------------------------------------")


if __name__ == "__main__":
    main()
