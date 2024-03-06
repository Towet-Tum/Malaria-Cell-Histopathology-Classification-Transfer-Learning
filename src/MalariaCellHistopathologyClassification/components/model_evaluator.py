import tensorflow as tf
from pathlib import Path
import mlflow
import mlflow.keras
from urllib.parse import urlparse
from MalariaCellHistopathologyClassification.utils.common import (
    load__process_dataset,
    save_json,
)
from MalariaCellHistopathologyClassification.entity.config_entity import (
    EvaluationConfig,
)


class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)

    def evaluation(self):
        _, _, test_ds, class_names = load__process_dataset(self.config.dataset)
        self.model = self.load_model(self.config.model_path)
        self.score = self.model.evaluate(test_ds)
        self.save_score()

    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)

    def log_into_mlflow(self):
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme

        with mlflow.start_run():
            mlflow.log_params(self.config.all_params)
            mlflow.log_metrics({"loss": self.score[0], "accuracy": self.score[1]})
            # Model registry does not work with file store
            if tracking_url_type_store != "file":

                mlflow.keras.log_model(
                    self.model, "model", registered_model_name="VGG19-Malaria-Cell"
                )
            else:
                mlflow.keras.log_model(self.model, "model")
