from cnnClassifierKidneyDisease.config.configuration import ConfigurationManager
from cnnClassifierKidneyDisease.components.data_ingestion import DataIngestion
from cnnClassifierKidneyDisease.logging import logger
from cnnClassifierKidneyDisease.utils.common import get_size

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            data_ingestion_config = config_manager.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            downloaded_path = data_ingestion.download_kaggle_data()
            logger.info(f"Size of downloaded data: {get_size(downloaded_path)}")
        except Exception as e:
            logger.error(f"An error occurred during data ingestion: {str(e)}")

if __name__ == "__main__":
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")