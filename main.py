from MalariaCellHistopathologyClassification import logger
from MalariaCellHistopathologyClassification.pipeline.stage_01_data_ingestion import (
    DataIngestionPipeline,
)
from MalariaCellHistopathologyClassification.pipeline.stage_02_model_trainer import (
    TrainingPipeline,
)

STAGE_NAME = "Data Ingestion Satge"
try:
    logger.info(f"\n\n <<<<<<<<< The {STAGE_NAME} has started >>>>>>>>>>>>>> \n\n")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(
        f" \n\n <<<<<<<<< The {STAGE_NAME} has completed successfully >>>>>>>>>>>>> \n\n =========="
    )
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training Stage"
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
