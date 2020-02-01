import os
import pandas as pd
import pickle
import math
from fbprophet import Prophet
from ProphetDatasetHelper import ProphetDatasetHelper
from model_constants import const


class ProphetModel():
    def __init__(self):
        self.dataset = ProphetDatasetHelper()

    def load_model(self, zone_id):
        model_path = os.path.join(const.data_files_folder, str(zone_id)+'.pkl')
        if os.path.isfile(model_path):
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            return model
        else:
            model = Prophet()
            rand_df = pd.read_csv(const.fbprophet_dataset_path)
            model.fit(rand_df)
            with open(model_path, 'wb') as f:
                pickle.dump(model, f)
            return model

    def get_predictions(self, zones_list):
        predictions = []
        for zone in zones_list:
            model = self.load_model(zone['zone_id'])
            future_dict = {
                'ds': [zone['predict_time']]
            }
            forecast = model.predict(pd.DataFrame(data=future_dict))
            predictions.append({
                'zone_id': zone['zone_id'],
                'predicted_people_count': math.floor(forecast['yhat'][0]),
                'prediction_probability': forecast['yhat_lower'][0]/forecast['yhat_upper'][0]
            })
        self.dataset.update_dataset_df(zones_list)
        return predictions