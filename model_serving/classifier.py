import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import ResNet50, preprocess_input, decode_predictions
from flask import Flask, request, jsonify
import numpy as np
MODEL_SERVING_HOST = '0.0.0.0'
MODEL_SERVING_PORT = 5003


# Load pre-trained ResNet50 model + higher level layers
base_model = ResNet50(weights='imagenet')

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the ResNet50 predictor. Send a POST request with an image to /predict to get predictions."

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file provided'}), 400

        # Get the image from the POST request
        image = tf.image.decode_image(request.files.get('file').read(), channels=3)
        image = tf.image.resize(image, [224, 224])
        
        # Preprocess & predict
        image_array = np.array(np.expand_dims(image.numpy(), axis=0))
        image_array = preprocess_input(image_array)
        predictions = base_model.predict(image_array)
        decoded_predictions = decode_predictions(predictions, top=5)[0]
        
        # Convert decoded_predictions to a serializable format
        serializable_predictions = []
        for label, name, score in decoded_predictions:
            serializable_predictions.append({
                "label": label,
                "name": name,
                "score": float(score)  # Convert float32 to native Python float
            })
        
        return jsonify(serializable_predictions)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico')

if __name__ == '__main__':
    app.run(host=MODEL_SERVING_HOST, port=MODEL_SERVING_PORT, debug=True)

