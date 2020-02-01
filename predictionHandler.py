import tornado.web
import json
from CatboostModel import PredictionModel
from FProphetModel import ProphetModel
from model_constants import const


class PredictionHandler(tornado.web.RequestHandler):
    def initialize(self):
        self.model = ProphetModel()

    def post(self):
        zones_list = json.loads(self.request.body)
        predictions = self.model.get_predictions(zones_list)
        self.write({'predictions': predictions})
