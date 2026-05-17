from cnnClassifierKidneyDisease.pipeline.01_data_ingestion_pipeline import DataIngestionPipeline
from cnnClassifierKidneyDisease.pipeline.02_prepare_base_model_pipeline import PrepareBaseModelPipeline 
from cnnClassifierKidneyDisease.logging import logger

STAGE_NAME = "Data Ingestion Stage"

logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
data_ingestion_pipeline = DataIngestionPipeline()
data_ingestion_pipeline.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")

STAGE_NAME = "Prepare Base Model Stage"
logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
prepare_base_model_pipeline = PrepareBaseModelPipeline()
prepare_base_model_pipeline.main()
logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")