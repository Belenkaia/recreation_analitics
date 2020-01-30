from catboost import Pool, CatBoostClassifier
import pandas as pd
from model_constants import const


class Prediction_model():
    def generate_new_model():
        train_df = pd.read_csv(const.dataset_path)
        labels_series = train_df['labels']
        del train_df['labels']

        train_dataset = Pool(data=train_df, label=labels_series)

        model = CatBoostClassifier(iterations=10,
                                   learning_rate=1,
                                   depth=2,
                                   loss_function='MultiClass')
        model.fit(train_dataset)
        model.save_model(const.model_path)

