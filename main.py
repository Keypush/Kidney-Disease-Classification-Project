from cnnClassifierKidneyDisease.pipeline.01_data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifierKidneyDisease.logging import logger

STAGE_NAME = "Data Ingestion Stage"

logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
data_ingestion_pipeline = DataIngestionPipeline()
data_ingestion_pipeline.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")