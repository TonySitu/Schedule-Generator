# Class models a schedule
# Tony Situ 
# 2023-06-15

from datetime import timedelta, time

class Schedule:
    def __init__(self, course_list: list):
        self._course_list = course_list
        self._rating = self.__rate()

    def __str__(self):
        return "Schedule Rating: " + str(self._rating) + "\nCourses: \n{}".format\
            ("\n".join([repr(course) for course in self._course_list]))

    def get_course_list(self) -> list:
        return self._course_list
    
    def get_rating(self) -> int:
        return self._rating

    def get_crn(self) -> list:
        return [course.get_crn() for course in self._course_list]
    
    def __rate(self) -> int:
        _835 = time(8, 35)
        _1005 = time(10, 5)
        _1135 = time(11, 35)
        courses_per_weekday = {"Mon": 0, "Tue": 0, "Wed": 0, "Thu": 0, "Fri": 0}
        rating = 0
        criteria = dict()
        criteria_file = open("User Data/Criteria.txt")
        criteria_file_lines = criteria_file.readlines()[1:]

        for index, lines in enumerate(criteria_file_lines):
            line = lines.strip().split(":")

            for word in range(len(line)):
                line[word] = line[word].strip()

            criteria[index] = line[1]
        
        criteria_file.close()

        sorted_course = sorted(self._course_list, key=lambda obj: obj.get_start_time())
        for course in sorted_course:
            if course.get_start_time().time() == _835:      # morning classes
                rating += 0
            if course.get_start_time().time() == _1005:     # morning classes
                rating += 0
            if course.get_start_time().time() == _1135:     # morning classes
                rating += 0

            for other_course in sorted_course[1:len(sorted_course)]:
                if course.has_day_conflict(other_course):
                    if (other_course.get_start_time() - course.get_start_time()) > timedelta(hours=2):      # if gap
                        rating += 0
            
            if time(13, 00) <= course.get_end_time().time() <= time(20, 00):     # if late afternoon
                rating += 0

            for weekday in courses_per_weekday.keys():
                if weekday in course.get_days():
                    courses_per_weekday[weekday] += 1
        
        # Everything after this line doesn't quite work as expected
        for day, num_courses in courses_per_weekday.items():
            if day == "Fri" and num_courses > 3:               # if specific day has one course
                rating -= 0
            if day == "Mon" and num_courses > 3:               # if specific day has one course
                rating -= 0
            if num_courses > 2:                                 # if courses at any day is greater than 2
                rating -= 8000
                if num_courses > 3:                             # if courses at any day is greater than 3
                    rating -= 8000

        return rating