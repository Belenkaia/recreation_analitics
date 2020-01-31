from GenerateModel import PredictionModel
from DatasetHelpers import DatasetHelper
from model_constants import const


dataset = DatasetHelper()
# dataset.generate_random_dataset(250)
dataset.generate_dataset_labels()

# model = PredictionModel(const.model_path)
# model.crossvalidate_dataset(const.dataset_path)
