from MalariaCellHistopathologyClassification import logger
from MalariaCellHistopathologyClassification.config.configuration import (
    ConfigurationManager,
)
from MalariaCellHistopathologyClassification.components.model_evaluator import (
    Evaluation,
)

STAGE_NAME = "Evaluation Stage"


class EvaluationPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_evaluation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.log_into_mlflow()


if __name__ == "__main__":
    try:
        logger.info(f"\n\n <<<<<<<<< The {STAGE_NAME} has started >>>>>>>>>>>>>> \n\n")
        evaluations = EvaluationPipeline()
        evaluations.main()
        logger.info(
            f" \n\n <<<<<<<<< The {STAGE_NAME} has completed successfully >>>>>>>>>>>>> \n\n =========="
        )
    except Exception as e:
        logger.exception(e)
        raise e
