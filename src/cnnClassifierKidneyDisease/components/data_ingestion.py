import os
import kagglehub
from cnnClassifierKidneyDisease.logging import logger
from cnnClassifierKidneyDisease.utils.common import get_size
from cnnClassifierKidneyDisease.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config
    
    def download_kaggle_data(self) -> str:
        '''
        Fetches the data from Kaggle using the provided URL in the configuration and saves it to the specified local path.
        
        returns:
            str: The path where the data has been downloaded.
        '''
        try:
            os.makedirs(os.path.dirname(self.config.unzip_dir), exist_ok=True )
            os.environ["KAGGLEHUB_CACHE"] = self.config.unzip_dir

            logger.info(f"Starting download of data from Kaggle: {self.config.kaggle_dataset}")  

            cache_path = kagglehub.dataset_download(self.config.kaggle_dataset)
            
            logger.info(f"Data downloaded to: {cache_path}")
            return cache_path
        except Exception as e:
            logger.error(f"Error occurred while downloading data from Kaggle: {self.config.kaggle_dataset}")
            raise e