import json
from datetime import datetime, timedelta


class ScheduleHelper:
    def __init__(self):
        with open("schedule.json") as data:
            self.schedule_dict = json.load(data)
            data.close()
        # convert strings to time
        hours, minutes = self.schedule_dict['classes_length'].split(':')
        self.classes_length = timedelta(hours=int(hours), minutes=int(minutes))
        self.start_times = []
        for start_time in self.schedule_dict['classes_start_time']:
            new_time = datetime.strptime(start_time, "%H:%M")
            self.start_times.append(new_time)

    def isOccupied(self, classroom_id, check_time):
        classes = self.schedule_dict[classroom_id]
        for class_num in classes:
            start_time = self.start_times[int(class_num) - 1]
            if start_time <= check_time and check_time <= start_time + self.classes_length:
                return True
        return False

    def test_schedule(self, all_classrooms):
        start_time = datetime.strptime("9:00", "%H:%M")
        end_time = datetime.strptime("23:00", "%H:%M")
        while start_time < end_time:
            print(start_time.strftime('%H:%M'))
            for classroom in all_classrooms:
                id = str(classroom['id'])
                isOccupied = self.isOccupied(id, start_time)
                print(id + ' - ' + str(isOccupied))
            print('-----------------------')
            start_time += timedelta(minutes=10)

