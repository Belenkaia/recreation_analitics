import json
from datetime import datetime, timedelta
import pytz
import math


class ScheduleHelper:
    def __init__(self):
        with open("current_schedule.json") as data:
            self.schedule_dict = json.load(data)
            data.close()
        # convert strings to time
        hours, minutes = self.schedule_dict['classes_length'].split(':')
        self.classes_length = timedelta(hours=int(hours), minutes=int(minutes))
        self.semestr_start_date = datetime.strptime(self.schedule_dict['semestr_start_date'], '%d/%m/%Y%z')
        self.start_times = []
        time_nsu = self.get_nsu_time()
        for start_time in self.schedule_dict['classes_start_time']:
            start_time += '|' + time_nsu.strftime('%D%z')  # Set Asia/Novosibirsk timezone
            new_time = datetime.strptime(start_time, "%H:%M|%m/%d/%y%z")
            self.start_times.append(new_time)
        self.count_class = 1

    def get_nsu_time(self):
        utc_time = datetime.utcnow()
        tz = pytz.timezone('Asia/Novosibirsk')
        return pytz.utc.localize(utc_time, is_dst=None).astimezone(tz)

    def get_current_weekday(self, check_date):
        delta = check_date - self.semestr_start_date
        week_num = math.floor(delta.days/7) + 1
        check_weekday = check_date.weekday() + 1
        if week_num % 2 == 0:
            return check_weekday
        else:
            # There is sunday for the odd weeks, but not for the even weeks
            if check_weekday == 7:
                return 7
            return check_weekday + 7

    def is_occupied(self, classroom_id, check_time):
        classroom_id = classroom_id.strip()
        weekday = str(self.get_current_weekday(check_time))
        classes = self.schedule_dict[classroom_id][weekday]
        for class_num in classes:
            start_time = self.start_times[int(class_num) - 1]
            if start_time <= check_time <= start_time + self.classes_length:
                return True
        return False
