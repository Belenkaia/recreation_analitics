import requests
from requests.auth import HTTPBasicAuth
import json


class ScheduleAPI:
    def __init__(self):
        self.base_url = r'https://table.nsu.ru/api/'
        self.token = 'W8ExqZsX8T6jTp4y3kSfkVy2v7tOwoOA'
        self.rooms = [3113, 3110, 3107, 3114, 3115, 3151, 3153, 3119, 3118, 3117, 3116, 3120, 3122, 3123, 3144, 3140, 3141, 3142, 3143, 3214, 3215, 3218, 3217, 3216, 3213, 3220, 3212, 3222, 3211, 3207, 3210, 3223, 3231, 3206, 3205, 3232, 3204, 3203, 3233, 3234, 3273, 3237, 3238, 3239, 3272, 3271, 3270, 3269, 3268, 3249, 3250, 3266, 3251, 3253, 3263, 3255, 3264, 3265, 3252, 3256, 3262, 3261, 3260, 3259, 3258, 3307, 3312, 3310, 3313, 3353, 3314, 3313, 3315, 3316, 3351, 3353, 3318, 3317, 3343, 3319, 3342, 3258, 3337, 3338, 3339, 3340, 3341]

    def get_groups_schedule(self, page):
        resp = requests.get(self.base_url + r'groups?expand=schedule&page=' + str(page),
                            auth=HTTPBasicAuth(self.token, ''))
        json_text = resp.text
        groups_dict = json.loads(json_text)
        return groups_dict

    def get_base_schedule_dict(self):
        schedule_dict = {
            "semestr_start_date": "01/09/2019+0700",
            "total_classes": 7,
            "classes_length": "1:35",
            "classes_start_time": ["9:00", "10:50", "12:40", "14:30", "16:20", "18:10", "20:00"],
        }
        for room in self.rooms:
            schedule_dict[str(room)] = {}
            for i in range(1, 14):
                schedule_dict[str(room)][str(i)] = []
        return schedule_dict

    def write_schedule_json(self, file_name):
        schedule_dict = self.get_base_schedule_dict()
        prev_id = -1
        current_id = 0
        current_page = 1
        while not prev_id == current_id:
            groups_dict = self.get_groups_schedule(current_page)
            for group in groups_dict:
                for day in group['schedule']:
                    room = day['room']
                    if room in schedule_dict:
                        weekday = day['weekday']
                        time_id = int(day['time']['id'])
                        # Sometimes there are more than one group in the class
                        if time_id not in schedule_dict[room][weekday]:
                            schedule_dict[room][weekday].append(time_id)
            current_page += 1
            prev_id = current_id
            current_id = groups_dict[0]['id']

        with open(file_name, 'w') as f:
            json.dump(schedule_dict, f)
