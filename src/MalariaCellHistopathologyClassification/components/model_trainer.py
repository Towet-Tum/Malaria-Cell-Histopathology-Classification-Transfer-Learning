import tensorflow as tf
import numpy as np
from MalariaCellHistopathologyClassification.utils.common import (
    load__process_dataset,
    save_plot,
)
from MalariaCellHistopathologyClassification.entity.config_entity import TrainingConfig


class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def train(self):
        train_ds, val_ds, _, _ = load__process_dataset(
            self.config.dataset, self.config.batch_size, self.config.img_size
        )
        preprocess_input = tf.keras.applications.vgg19.preprocess_input
        IMG_SHAPE = (224, 224, 3)
        base_model = tf.keras.applications.VGG19(
            input_shape=IMG_SHAPE, include_top=False, weights="imagenet"
        )
        image_batch, label_batch = next(iter(train_ds))
        feature_batch = base_model(image_batch)

        for layer in base_model.layers:
            layer.tranable = False

        global_average_layer = tf.keras.layers.GlobalAveragePooling2D()
        feature_batch_average = global_average_layer(feature_batch)
        prediction_layer = tf.keras.layers.Dense(1)
        prediction_batch = prediction_layer(feature_batch_average)

        inputs = tf.keras.Input(shape=(224, 224, 3))
        x = preprocess_input(inputs)
        x = base_model(x, training=False)
        x = global_average_layer(x)
        x = tf.keras.layers.Dropout(0.2)(x)
        outputs = prediction_layer(x)
        model = tf.keras.Model(inputs, outputs)

        model.compile(
            optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
            loss=tf.keras.losses.BinaryCrossentropy(from_logits=True),
            metrics=[tf.keras.metrics.BinaryAccuracy(threshold=0, name="accuracy")],
        )

        history = model.fit(
            train_ds,
            epochs=self.config.epochs,
            steps_per_epoch=len(train_ds) / 32,
            validation_data=val_ds,
            validation_steps=len(val_ds) / 32,
            verbose=1,
        )
        model.save(
            "src/MalariaCellHistopathologyClassification/models/train_weights.py/Malaria_cell_TF.h5"
        )
        save_plot(
            history,
            "src/MalariaCellHistopathologyClassification/models/plots.py/history.png",
        )
