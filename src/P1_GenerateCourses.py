# Class generates a list of courses
# Tony Situ 
# 2023-06-13

from datetime import datetime
from Course import Course
import os


def __create_tutorial_dict() -> dict:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    user_data_dir = os.path.join(current_dir, "..", "UserData")
    tutorial_dir = os.path.join(user_data_dir, "Tutorials.txt")

    with open(tutorial_dir, "r") as tutorial_file:
        tutorial_file_lines = tutorial_file.readlines()[1:]

    add_tutorial = False
    tutorial_dict = __wrap_line(tutorial_file_lines, add_tutorial)

    return tutorial_dict


def create_course_dict() -> dict:
    tutorial_dict = __create_tutorial_dict()

    current_dir = os.path.dirname(os.path.realpath(__file__))
    user_data_dir = os.path.join(current_dir, "..", "UserData")
    course_dir = os.path.join(user_data_dir, "Courses.txt")

    with open(course_dir, "r") as course_file:
        course_file_lines = course_file.readlines()[1:]

    add_tutorial = True
    course_dict = __wrap_line(course_file_lines, add_tutorial, tutorial_dict)

    return course_dict


def __wrap_line(lines: list, add_tutorials: bool, tutorial_dict=None) -> dict:
    """
    Receive a list of lines from a file and puts them into a dictionary
    to return
    """
    if add_tutorials and tutorial_dict is None:
        raise ValueError("Cannot add tutorials to courses with empty tutorial dictionary")

    dictionary = dict()

    for line in lines:
        line = line.strip("\n").split(",")

        course = __create_course(line)

        if add_tutorials:
            if tutorial_dict.get(course.get_code()) is not None:
                for tutorial in tutorial_dict[course.get_code()]:
                    if course.get_section() in tutorial.get_section_tie():
                        if course.get_tutorials() is None:
                            course.set_tutorial()
                        course.add_tutorial(tutorial)

        if not dictionary.get(course.get_code()):
            dictionary[course.get_code()] = []

        dictionary[course.get_code()].append(course)

    return dictionary


def __create_course(line: str) -> Course:
    """
    Takes in a line that creates a course based off of info from line
    """
    days = line[3].split()
    start_time = datetime.strptime(line[4].strip(), '%H:%M')
    end_time = datetime.strptime(line[5].strip(), '%H:%M')

    return Course(line[0], line[1], line[2], days, start_time, end_time, line[6])


def main() -> None:
    course_dict = create_course_dict()
    for k, v in course_dict.items():
        print(k, ":", str(v))


if __name__ == "__main__":
    main()
