# Class generates a list of schedules
# Tony Situ 
# 2023-06-15

from P2_GenerateSchedules import create_course_dict
from datetime import time, timedelta
import pickle
import os

class PrintSchedule:
    def __init__(self):
        self._schedule_counter = None
        self._schedules = self.__get_schedules()

    def __get_schedules(self) -> list:
        generator = GenerateSchedules()
        schedules = generator.get_schedules()
        schedule1, schedule2, schedule3 = schedules[0], schedules[1], schedules[2]
        return list((schedule1, schedule2, schedule3))
    
    def __get_schedule_count(self) -> None:
        counter_file = "ScheduleCounter.pkl"
        file_path = os.path.join("data", counter_file)

        try: 
            with open(file_path, "rb") as file:
                self._schedule_counter = pickle.load(file)
        except:
            with open(file_path, "wb") as file:
                self._schedule_counter = 1
                pickle.dump(self._schedule_counter, file)
    
    def print_schedules(self):
        self.__get_schedule_count()
        string = ""
        weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]
        for index in range (3):
            string += "{0: ^6}|".format("Time")
            for day_of_week in weekdays:
                string += "{0: ^21}|".format(day_of_week)

            string += "\n" + "-"*119

            for timing in range(8, 21):
                for increment_time in range(0, 60, 30):
                    time_block = time(timing, increment_time)
                    string += "\n\n" + "{0: ^7}|".format(time_block.strftime('%H:%M'))
                    for weekday in weekdays:
                        found_course = False
                        for course in self._schedules[index].get_course_list():

                            if (course.get_start_time() - timedelta(minutes=5)).time() <= time_block <= course.get_end_time().time() \
                                and weekday in course.get_days():
                                string += "{0: ^21}|".format(course.get_code() + course.get_section())
                                found_course = True

                        if found_course is False:
                            string += "{0: ^21}|".format("")
            string += f"\n\n{self._schedules[index]}"
            string += "Course Codes: {}\n".format(", ".join(code for code in self._schedules[index].get_code_list()))
            string += "Crn List: {}\n\n".format(", ".join(str(crn) for crn in self._schedules[index].get_crn()))
            print(string, end="")

        output_file = "Schedule_" + str(self._schedule_counter) + ".txt"

        self._schedule_counter += 1
        counter_file = "ScheduleCounter.pkl"
        file_path = os.path.join("data", counter_file)

        with open(file_path, "wb") as file:
                pickle.dump(self._schedule_counter, file)

        file_path = os.path.join("GeneratedSchedules", output_file)
        with open(file_path, "w") as file:
            file.write(string)

def main():
    PrintSchedule().print_schedules()

if __name__ == "__main__":
    main()