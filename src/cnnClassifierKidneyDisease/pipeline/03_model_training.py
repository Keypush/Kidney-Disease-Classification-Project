from cnnClassifierKidneyDisease.config.configuration import ConfigurationManager
from cnnClassifierKidneyDisease.components.model_training import ModelTraining, TrainingConfig
from cnnClassifierKidneyDisease.logging import logger
from cnnClassifierKidneyDisease.utils.common import get_size

STAGE_NAME = "Model Training Stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config_manager = ConfigurationManager()
            training_config = config_manager.get_training_config()
            model_training = ModelTraining(config=training_config)
            model_training.get_base_model()
            model_training.train_valid_generator()
            model_training.train(callbacks_list=None)
        except Exception as e:
            logger.error(f"An error occurred during model training: {str(e)}")

if __name__ == "__main__":
    logger.info(f">>>>>> Stage {STAGE_NAME} started <<<<<<")
    model_training_pipeline = ModelTrainingPipeline()
    model_training_pipeline.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} completed <<<<<<\n\n")