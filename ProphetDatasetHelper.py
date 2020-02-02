import os
import pandas as pd
from model_constants import const

class ProphetDatasetHelper():
    def get_zone_dataset_path(self, zone_id):
        dataset_path = os.path.join(const.data_files_folder, str(zone_id)+'.csv')
        if os.path.isfile(dataset_path):
            return dataset_path
        else:
            with open(dataset_path, 'w') as f:
                f.write('ds,y')
                f.close()
            return dataset_path

    def update_dataset_df(self, zones_list):
        for zone in zones_list:
            zone_dataset_path = self.get_zone_dataset_path(zone['zoneid'])
            dataset_df = pd.read_csv(zone_dataset_path)
            new_dict = {
                'ds': [zone['curr_timestamp']],
                'y': [zone['curr_people_count']]
            }
            new_df = pd.DataFrame(data=new_dict)
            dataset_df = dataset_df.append(new_df)
            dataset_df.to_csv(zone_dataset_path, index=False)

    def get_dataset_df(self, zone_id):
        dataset_path = self.get_zone_dataset_path(zone_id)
        return pd.read_csv(dataset_path)
