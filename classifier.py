import tensorflow as tf
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from flask import Flask, request, jsonify
import numpy as np

# Load pre-trained ResNet50 model + higher level layers
base_model = ResNet50(weights='imagenet')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the POST request
    image = tf.image.decode_image(request.files.get('file').read(), channels=3)
    image = tf.image.resize(image, [224, 224])
    
    # Preprocess & predict
    image_array = np.expand_dims(image, axis=0)
    image_array = preprocess_input(image_array)
    predictions = base_model.predict(image_array)
    decoded_predictions = decode_predictions(predictions, top=5)[0]
    
    return jsonify(decoded_predictions)

if __name__ == '__main__':
    app.run(port=5000, debug=True)
