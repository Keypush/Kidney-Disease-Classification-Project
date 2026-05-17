from cnnClassifierKidneyDisease.constants import *
from cnnClassifierKidneyDisease.utils.common import read_yaml, create_directories
from cnnClassifierKidneyDisease.entity.config_entity import (DataIngestionConfig,
                                                        PrepareBaseModelConfig, TrainingConfig)     

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
    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            updated_base_model_path=config.updated_base_model_path,
            params_image_size=self.params.IMAGE_SIZE,
            params_learning_rate=self.params.LEARNING_RATE,
            params_including_top=self.params.INCLUDING_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_augmentation=self.params.AUGMENTATION
        )

        return prepare_base_model_config
    
    def get_training_config(self) -> TrainingConfig:
        training_config = self.config.model_training
        prepare_base_model_config = self.config.prepare_base_model
        training_data = Path(self.config.data_ingestion.unzip_dir)
        
        create_directories([training_config.root_dir])

        training_config = TrainingConfig(
            root_dir=training_config.root_dir,
            trained_model_path=training_config.trained_model_path,
            updated_base_model_path=prepare_base_model_config.updated_base_model_path,
            training_data_dir=training_data,
            params_image_size=self.params.IMAGE_SIZE,
            params_epochs=self.params.EPOCHS,
            params_batch_size=self.params.BATCH_SIZE,
            params_augmentation=self.params.AUGMENTATION
        )

        return training_config