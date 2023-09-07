# Class generates a list of schedules
# Tony Situ 
# 2023-06-13

from P1_GenerateCourses import GenerateCourses
import itertools
from Schedule import Schedule
from BinaryMaxHeap import BinaryMaxHeap

class GenerateSchedules:
    def __init__(self):
        self._num_schedules = 0
        self._schedules = self.__create_schedules()

    def __create_schedules(self) -> list:
        schedules = BinaryMaxHeap()
        course_generator = GenerateCourses("Courses.txt", "Tutorials.txt")
        course_dict = course_generator.get_course_dict()

        for combinations_of_courses in itertools.product(*course_dict.values()):
            course_list = list(combinations_of_courses)                               # courses refers to the schedule of courses generated
        
            tutorial_schedules = []
            for course in course_list:                                                # iterates through courses in schedule
                tutorial_schedules.append(course.get_tutorials())                     # adds a list of tutorials into a dict

            for combinations_of_tutorials in itertools.product(*tutorial_schedules):
                tutorial_list = list(combinations_of_tutorials)
                final_schedule = Schedule(course_list + tutorial_list)

                is_valid = self.__is_valid_schedule(final_schedule.get_course_list())
                if is_valid is True:
                    schedules.add(final_schedule)
                    self._num_schedules += 1

        return schedules
    
    def __is_valid_schedule(self, schedule: list) -> bool:
        for index, course in enumerate(schedule):                           # iterates through courses in schedule
            for other_course in schedule[index + 1: len(schedule)]:   
                if course.has_conflict(other_course):                       # checks if schedule has time conflicts
                    return False

        return True
    
    def get_schedules(self) -> list:
        return self._schedules
    
    def get_num_schedules(self) -> int:
        return self._num_schedules

def main() -> None:
    generator = GenerateSchedules()
    schedules = generator.get_schedules()
    print("----------------------------------------------------------------------")
    for schedule in schedules:
        print(str(schedule) + "\n")

    print("number of schedules", len(schedules))
    print("----------------------------------------------------------------------")

if __name__ == "__main__":
    main()