import json
from datetime import datetime, timedelta, timezone
import pytz
import pandas as pd
import random


class ScheduleHelper:
    def __init__(self):
        with open("schedule.json") as data:
            self.schedule_dict = json.load(data)
            data.close()
        # convert strings to time
        hours, minutes = self.schedule_dict['classes_length'].split(':')
        self.classes_length = timedelta(hours=int(hours), minutes=int(minutes))
        self.start_times = []
        time_nsu = self.get_nsu_time()
        for start_time in self.schedule_dict['classes_start_time']:
            start_time += '|' + time_nsu.strftime('%D%z')  # Set Asia/Novosibirsk timezone
            new_time = datetime.strptime(start_time, "%H:%M|%m/%d/%y%z")
            self.start_times.append(new_time)

    def get_nsu_time(self):
        utc_time = datetime.utcnow()
        tz = pytz.timezone('Asia/Novosibirsk')
        return pytz.utc.localize(utc_time, is_dst=None).astimezone(tz)

    def is_occupied(self, classroom_id, check_time):
        classroom_id = classroom_id.strip()
        classes = self.schedule_dict[classroom_id]
        for class_num in classes:
            start_time = self.start_times[int(class_num) - 1]
            if start_time <= check_time and check_time <= start_time + self.classes_length:
                return True
        return False
