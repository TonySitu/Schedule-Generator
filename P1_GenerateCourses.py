# Class generates a list of courses
# Tony Situ 
# 2023-06-13

from datetime import datetime
from Course import Course


class GenerateCourses:
    def __init__(self, course_file: str, tutorial_file: str) -> None:
        self._course_file = course_file
        self._tutorial_file = tutorial_file
        self._course_dict = self.__create_courses()

    def __create_tutorial_dict(self) -> dict:
        tutorial_dict = dict()
        tutorial_file = open("UserData/" + self._tutorial_file)
        tutorial_file_lines = tutorial_file.readlines()[1:]

        for lines in tutorial_file_lines:
            line = lines.strip("\n").split(",")

            for word in range(len(line)):
                line[word] = line[word].strip()

            days = line[3].split()
            start_time = datetime.strptime(line[4], '%H:%M')
            end_time = datetime.strptime(line[5], '%H:%M')

            tutorial = Course(line[0], line[1], line[2], days, start_time, end_time, line[6])

            if tutorial_dict.get(tutorial.get_code()):
                tutorial_dict[tutorial.get_code()].append(tutorial)
            else:
                tutorial_dict[tutorial.get_code()] = [tutorial]

        tutorial_file.close()
        return tutorial_dict

    def __create_courses(self) -> dict:
        course_file = open("UserData/" + self._course_file)
        course_file_lines = course_file.readlines()[1:]

        tutorial_dict = self.__create_tutorial_dict()
        course_dict = dict()

        for lines in course_file_lines:
            line = lines.strip().split(",")

            for word in range(len(line)):
                line[word] = line[word].strip()

            days = line[3].split()
            start_time = datetime.strptime(line[4], '%H:%M')
            end_time = datetime.strptime(line[5], '%H:%M')

            course = Course(line[0], line[1], line[2], days, start_time, end_time, line[6])

            temp_list = []
            if tutorial_dict.get(course.get_code()) is not None:
                for tutorial in tutorial_dict[course.get_code()]:
                    if (course.get_section() in tutorial.get_section_tie()):
                        temp_list.append(tutorial)
                course.add_tutorial(temp_list)

            if course_dict.get(course.get_code()):
                course_dict[course.get_code()].append(course)
            else:
                course_dict[course.get_code()] = [course]

        course_file.close()
        return course_dict

    def get_course_dict(self) -> dict:
        return self._course_dict


def main() -> None:
    gen = GenerateCourses("Courses.txt", "Tutorials.txt")
    course_dict = gen.get_course_dict()
    for k, v in course_dict.items():
        print(k, ":", str(v))


if __name__ == "__main__":
    main()
