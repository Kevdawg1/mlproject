import os, sys
from src.exception.exception import MLException
from src.logging.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split

from src.config.config_entities import DataIngestionConfig
from src.constants.training_pipeline import DATA_DIR, FILE_NAME


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info('Data Ingestion method started')
        try:
            file_path = os.path.join(DATA_DIR, FILE_NAME)
            df = pd.read_csv(file_path)
            logging.info('Dataset read as pandas DataFrame')
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info('Train test split initiated')
            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)
            logging.info('Ingestion of data is completed')
            
            return (
                self.ingestion_config.train_data_path, 
                self.ingestion_config.test_data_path, 
                self.ingestion_config.raw_data_path
            )
        except Exception as e:
            raise MLException(e, sys)
        
        
if __name__ == "__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()