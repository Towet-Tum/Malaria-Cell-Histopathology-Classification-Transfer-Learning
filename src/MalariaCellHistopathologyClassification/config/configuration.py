from MalariaCellHistopathologyClassification.constants import *
from MalariaCellHistopathologyClassification.utils.common import (
    create_directories,
    read_yaml,
)
from MalariaCellHistopathologyClassification.entity.config_entity import (
    DataIngestionConfig,
    TrainingConfig,
)


class ConfigurationManager:
    def __init__(
        self, config_file_path=CONFIG_FILE_PATH, param_file_path=PARAMS_FILE_PATH
    ):
        self.config = read_yaml(config_file_path)
        self.param = read_yaml(param_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir,
        )

        return data_ingestion_config

    def get_training_config(self) -> TrainingConfig:
        config = self.config.training
        param = self.param
        create_directories([config.root_dir])
        dataset = "artifacts/data_ingestion/dataset/"
        training_config = TrainingConfig(
            root_dir=config.root_dir,
            model_path=config.model_path,
            epochs=param.EPOCH,
            base_model=param.BASE_MODEL,
            img_size=param.IMG_SIZE,
            batch_size=param.BATCH_SIZE,
            optimizer=param.OPTIMIZER,
            loss=param.LOSS,
            metrics=param.METRICS,
            dataset=str(dataset),
        )
        return training_config
