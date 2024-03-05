from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: Path
    local_data_file: Path
    unzip_dir: Path


from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    model_path: Path
    dataset: Path
    epochs: int
    loss: str
    optimizer: str
    base_model: str
    batch_size: int
    metrics: list
    img_size: tuple
