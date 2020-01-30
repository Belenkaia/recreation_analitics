import catboost
from catboost import CatBoostClassifier
import json
import time
from datetime import datetime, timedelta
from scheduleHelper import ScheduleHelper
from MapTableReader import get_map_dictionary


map_dict = get_map_dictionary()
print(map_dict)
