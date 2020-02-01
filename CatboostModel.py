from catboost import Pool, CatBoostRegressor, cv
import pandas as pd
from model_constants import const


class PredictionModel():
    def __init__(self, model_path=None):
        if model_path == None:
            self.model_path = const.model_path
            self.generate_new_model()
        else:
            self.model_path = model_path
            self.model = self.get_empty_model()
            self.model.load_model(model_path)

    def get_empty_model(self):
        return CatBoostRegressor(**const.catboost_params)

    def generate_new_model(self):
        train_df = pd.read_csv(const.dataset_path)
        labels_series = pd.read_csv(const.labels_path, header=None)

        train_dataset = Pool(data=train_df, label=labels_series)
        self.model = self.get_empty_model()
        self.model.fit(train_dataset)
        self.model.save_model(self.model_path)

    def crossvalidate_dataset(self):
        train_df = pd.read_csv(const.dataset_path)
        labels_series = pd.read_csv(const.labels_path, header=None)

        cv_dataset = Pool(train_df, labels_series)
        scores_df = cv(cv_dataset,
                       const.crossvalidation_params,
                       fold_count=2)
        scores_df.to_csv(r'C:\Users\user\Desktop\cv_scores.csv', index=False)

    def get_predictions(self, features_df):
        data_pool = Pool(features_df)
        predictions = self.model.predict(data_pool)
        return predictions.tolist()
