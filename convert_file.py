import tensorflowjs as tfjs
from tensorflow import keras

# Load your Keras model (replace with your model's loading method)
model = keras.models.load_model('./model/room_model_1552970840.h5')

# Save the model in TensorFlow.js format
tfjs.converters.save_keras_model(model, './model/tfjs_model')
