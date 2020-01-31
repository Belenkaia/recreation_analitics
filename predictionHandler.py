import tornado.web
import json
from CatboostModel import PredictionModel
from DatasetHelpers import DatasetHelper
from model_constants import const


class PredictionHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = PredictionModel(const.model_path)

    def post(self):
        zones_list = json.loads(self.get_body_argument('zones'))
        features_df = DatasetHelper().get_features_list(zones_list)