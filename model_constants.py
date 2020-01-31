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

        self.map_table_file = r'C:\Users\user\Desktop\recreation_analitics\data_files\mapTable.tsv'
        self.dataset_path = r'C:\Users\user\Desktop\recreation_analitics\data_files\dataset.csv'
        self.labels_path = r'C:\Users\user\Desktop\recreation_analitics\data_files\dataset_labels.csv'
        self.model_path = r'C:\Users\user\Desktop\recreation_analitics\data_files\prediction_model.cbm'

        self.catboost_params = {
            'iterations': 250,
            'depth': 6,
            'loss_function': 'RMSE'
        }
        self.crossvalidation_params = self.catboost_params


const = constants()
