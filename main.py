from GenerateModel import PredictionModel
from DatasetHelpers import DatasetHelper
from model_constants import const


model = PredictionModel(const.model_path)
model.crossvalidate_dataset(const.dataset_path)
