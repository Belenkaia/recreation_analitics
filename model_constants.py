import os
import pathlib

class constants:
    def __init__(self):
        self.traffic_col = 'traffic'
        self.class_col = 'class_coeff'
        self.size_col = 'size'
        self.sockets_col = 'sockets_size'
        self.popularity_col = 'popularity'
        self.occupancy_col = 'currentOccupancy'
        self.power_occupancy_col = 'powerOccupancy'
        self.dataset_header = [self.traffic_col, self.class_col, self.size_col, self.sockets_col, self.popularity_col,
                               self.occupancy_col, self.power_occupancy_col]

        self.traffic_importance = 3.0
        self.class_importance = 5.0
        self.size_importance = 1.0
        self.sockets_importance = 2.0
        self.popularity_importance = 2.0
        self.occupancy_importance = 4.0
        self.power_occupancy_importance = 4.0
        self.feature_weight = [self.traffic_importance, self.class_importance, self.size_importance, self.sockets_importance, self.popularity_importance,
                               self.occupancy_importance, self.power_occupancy_importance]

        self.data_files_folder = os.path.join(pathlib.Path(__file__).parent.absolute(), 'data_files')
        self.map_table_file = os.path.join(self.data_files_folder, 'mapTable.tsv')

        self.dataset_path = os.path.join(self.data_files_folder, 'dataset.csv')
        self.labels_path = os.path.join(self.data_files_folder, 'dataset_labels.csv')
        self.test_dataset_path = os.path.join(self.data_files_folder, 'test_dataset.csv')
        self.test_labels_path = os.path.join(self.data_files_folder, 'test_dataset_labels.csv')
        self.fbprophet_dataset_path = os.path.join(self.data_files_folder, 'fb_random_dataset.csv')

        self.model_path = os.path.join(self.data_files_folder, 'prediction_model.cbm')
        self.schedule_file = os.path.join(self.data_files_folder, 'current_schedule.json')
        self.daily_dataset_file = os.path.join(self.data_files_folder, 'current_schedule.json')

        self.catboost_params = {
            'iterations': 250,
            'depth': 6,
            'loss_function': 'RMSE'
        }
        self.crossvalidation_params = self.catboost_params


const = constants()
