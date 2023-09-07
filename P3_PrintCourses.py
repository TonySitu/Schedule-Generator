# Class generates a list of schedules
# Tony Situ 
# 2023-06-15

from P2_GenerateSchedules import GenerateSchedules
from datetime import time, timedelta

class PrintSchedule:
    def __init__(self):
        self._schedules = self.__get_schedules()

    def __get_schedules(self) -> list:
        generator = GenerateSchedules()
        schedules = generator.get_schedules()
        schedule1, schedule2, schedule3 = schedules[0], schedules[1], schedules[2]
        return list((schedule1, schedule2, schedule3))
    
    def print_schedules(self):
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        for index in range (3):
            print("\n {0: ^6}|".format("Time"), end='')
            for day_of_week in weekdays:
                print("{0: ^21}|".format(day_of_week), end='')
            print("\n" + "-"*119, end='')

            for timing in range(8, 21):
                for increment_time in range(0, 60, 30):
                    time_block = time(timing, increment_time)
                    print("\n\n" + "{0: ^7}|".format(time_block.strftime('%H:%M')), end='')
                    for weekday in weekdays:
                        found_course = False
                        for course in self._schedules[index].get_course_list():

                            if (course.get_start_time() - timedelta(minutes=5)).time() <= time_block <= course.get_end_time().time() \
                                and weekday in course.get_days():
                                print("{0: ^21}|".format(course.get_code() + course.get_section()), end='')
                                found_course = True

                        if found_course is False:
                            print("{0: ^21}|".format(""), end='')
            print(f"\n\n{self._schedules[index]}")
            print("Crn List: {}\n".format(", ".join(str(crn) for crn in self._schedules[index].get_crn())))

def main():
    PrintSchedule().print_schedules()

if __name__ == "__main__":
    main()