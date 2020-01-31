class constants:
    def __init__(self):
        self.traffic_col = 'traffic'
        self.class_col = 'class_coeff'
        self.size_col = 'size'
        self.sockets_col = 'sockets_size'
        self.popularity_col = 'popularity'
        self.occupancy_col = 'currentOccupancy'
        self.labels_col = 'label'

        self.traffic_importance = 3.0
        self.class_importance = 5.0
        self.size_importance = 1.0
        self.sockets_importance = 4.0
        self.popularity_importance = 2.0
        self.occupancy_importance = 4.0

        self.five_min_class = 1
        self.fiveteen_min_class = 2
        self.thirty_min_class = 3
        self.hour_min_class = 4

        self.dataset_path = r'C:\Users\user\Desktop\recreation_analitics\dataset.csv'
        self.test_path = r'C:\Users\user\Desktop\recreation_analitics\test_dataset.csv'
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
