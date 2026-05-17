from cnnClassifierKidneyDisease.constants import *
from cnnClassifierKidneyDisease.utils.common import read_yaml, create_directories
from cnnClassifierKidneyDisease.entity.config_entity import DataIngestionConfig

class ConfigurationManager:
    def __init__(
        self,
        config_file_path: Path = CONFIG_FILE_PATH,
        params_file_path: Path = PARAMS_FILE_PATH) -> None:
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        
        create_directories([self.config.artifacts_root])



    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            kaggle_dataset=config.kaggle_dataset,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config