# Class models a course
# Tony Situ 
# 2023-06-13

from datetime import datetime
import Course


class Course:
    def __init__(self, crn: str, code: str, section: str, days: list,
                 start_time: datetime, end_time: datetime, section_tie: str, tutorials=None) -> None:
        self._crn = crn
        self._code = code
        self._days = days
        self._section = section
        self._start_time = start_time
        self._end_time = end_time
        self._section_tie = section_tie
        self._tutorials = tutorials

    def __repr__(self) -> str:
        return "{} {} {} {} {} {}".format(self._crn, self._code, self._days, self._section,
                                          self._start_time.strftime('%H:%M'), self._end_time.strftime('%H:%M'))

    def set_tutorial(self):
        self._tutorials = []

    def add_tutorial(self, tutorial: Course) -> None:
        self._tutorials.append(tutorial)

    def has_conflict(self, other_course: Course) -> bool:
        return self.__has_time_conflict(other_course) and self.has_day_conflict(other_course)

    def has_day_conflict(self, other_course: Course) -> bool:
        common_days = set(self._days).intersection(other_course.get_days())
        return len(common_days) > 0

    def __has_time_conflict(self, other_course: Course) -> bool:
        return (other_course._start_time <= self._start_time <= other_course._end_time) \
            or self._start_time <= other_course._start_time <= self._end_time

    def get_tutorials(self) -> list:
        return self._tutorials

    def get_code(self) -> str:
        return self._code

    def get_crn(self) -> str:
        return self._crn

    def get_section(self) -> str:
        return self._section

    def get_section_tie(self) -> str:
        return self._section_tie

    def get_start_time(self) -> datetime:
        return self._start_time

    def get_end_time(self) -> datetime:
        return self._end_time

    def get_days(self) -> str:
        return self._days
