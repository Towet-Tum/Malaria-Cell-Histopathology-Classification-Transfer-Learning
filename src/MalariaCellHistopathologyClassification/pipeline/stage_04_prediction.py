import os
import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img


class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename

    def makePrediction(self):

        model = load_model(os.path.join("artifacts", "training", "Malaria_cell_TF.h5"))

        class_names = ["Parasitized", "Uninfected"]

        # Load and preprocess the image
        img = image.load_img(self.filename, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)

        # Predict using the model
        result = model.predict(img_array)
        prediction = tf.nn.sigmoid(result)
        predictions = tf.where(prediction < 0.5, 0, 1)

        # Get the predicted class index
        predicted_class_index = tf.argmax(predictions, axis=1).numpy()[0]

        name = class_names[int(predictions.numpy())]

        # prob = rounded_prediction.numpy()[0][0]
        prob = "%.2f" % prediction.numpy()[0][0]

        return name, prob


if __name__ == "__main__":
    img = "artifacts/data_ingestion/dataset/Uninfected/C1_thinF_IMG_20150604_104722_cell_9.png"

    pred = PredictionPipeline(img)
    name, pred = pred.makePrediction()
    print(f"The class Name:: {name}")
    print(f"The class Prob:: {pred}")
