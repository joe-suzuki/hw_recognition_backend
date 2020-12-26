import tensorflow as tf
import numpy as np


def predict(image):
    loaded_model = tf.keras.models.load_model("api/tensorflow/saved_models/simple_model.h5")
    prediction = loaded_model.predict(image)
    predicted_label = np.argmax(prediction)
    prediction_prob = prediction[0].tolist()

    return predicted_label, prediction_prob
