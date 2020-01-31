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

        self.dataset_path = r'C:\Users\user\Desktop\recreation_analitics\dataset.csv'
        self.labels_path = r'C:\Users\user\Desktop\recreation_analitics\dataset_labels.csv'
        self.model_path = r'C:\Users\user\Desktop\recreation_analitics\prediction_model.cbm'

        self.catboost_params = {
            'iterations': 20,
            'learning_rate': 1,
            'depth': 4,
            'loss_function': 'MultiClass'
        }
        self.crossvalidation_params = self.catboost_params
        self.crossvalidation_params['loss_function'] = 'Logloss'
        self.crossvalidation_params['roc_file'] = 'roc-file'


const = constants()
