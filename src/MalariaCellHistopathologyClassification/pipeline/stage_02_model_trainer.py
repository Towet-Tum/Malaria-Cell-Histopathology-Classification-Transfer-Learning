from MalariaCellHistopathologyClassification import logger
from MalariaCellHistopathologyClassification.components.model_trainer import Training
from MalariaCellHistopathologyClassification.config.configuration import (
    ConfigurationManager,
)

STAGE_NAME = "Training Stage"


class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        train_config = config.get_training_config()
        training = Training(config=train_config)
        training.train()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n <<<<<<<<< The {STAGE_NAME} has started >>>>>>>>>>>>>> \n\n")
        training = TrainingPipeline()
        training.main()
        logger.info(
            f" \n\n <<<<<<<<< The {STAGE_NAME} has completed successfully >>>>>>>>>>>>> \n\n =========="
        )
    except Exception as e:
        logger.exception(e)
        raise e
