from MalariaCellHistopathologyClassification import logger
from MalariaCellHistopathologyClassification.components.data_ingestion import (
    DataIngestion,
)
from MalariaCellHistopathologyClassification.config.configuration import (
    ConfigurationManager,
)

STAGE_NAME = "Data Ingestion Stage"


class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(config=data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()


if __name__ == "__main__":
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
