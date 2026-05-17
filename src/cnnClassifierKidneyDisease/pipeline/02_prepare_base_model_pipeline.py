from cnnClassifierKidneyDisease.config.configuration import ConfigurationManager
from cnnClassifierKidneyDisease.components.prepare_base_model import PrepareBaseModel, PrepareBaseModelConfig
from cnnClassifierKidneyDisease.logging import logger
from cnnClassifierKidneyDisease.utils.common import get_size

STAGE_NAME = "Prepare Base Model Stage"

class PrepareBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            prepare_base_model_config = config_manager.get_prepare_base_model_config()
            prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
            prepare_base_model.get_base_model()
            prepare_base_model.update_base_model()
        except Exception as e:
            logger.error(f"An error occurred during base model preparation: {str(e)}")

if __name__ == "__main__":
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    prepare_base_model_pipeline = PrepareBaseModelPipeline()
    prepare_base_model_pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")