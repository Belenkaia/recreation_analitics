import tornado.web
import json
from CatboostModel import PredictionModel
from DatasetHelpers import DatasetHelper
from model_constants import const


class PredictionHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = PredictionModel(const.model_path)
        self.dataset = DatasetHelper()
        self.isTraning = False
        with open('isTrainingWeek.txt') as f:
            if f.readline() == '1':
                self.isTraning = True

    def post(self):
        zones_list = json.loads(self.request.body)
        features_df = self.dataset.get_features_df(zones_list)
        predictions = self.model.get_predictions(features_df)
        self.write({'predictions': predictions})
        self.dataset.add_new_data(zones_list)
