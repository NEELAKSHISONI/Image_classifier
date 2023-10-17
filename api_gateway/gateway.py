from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

IMAGE_UPLOAD_SERVICE_URL = "http://localhost:5001"
IMAGE_PROCESSING_SERVICE_URL = "http://localhost:5002"
MODEL_SERVING_SERVICE_URL = "http://localhost:5003"
USER_MANAGEMENT_SERVICE_URL = "http://localhost:5004"

@app.route('/')
def index():
    return "Welcome to the Image Classifier API Gateway!"

@app.route('/full_classify', methods=['POST'])
def full_classify():
    try:
        # 1. Store the image
        upload_response = requests.post(IMAGE_UPLOAD_SERVICE_URL + '/upload', files=request.files)
        if upload_response.status_code != 200:
            return jsonify({'error': 'Failed to upload image'}), 500
        # Assuming the upload service returns the stored image or its reference
        stored_image = upload_response.content

        # 2. Preprocess the image
        preprocess_response = requests.post(IMAGE_PROCESSING_SERVICE_URL + '/process', files={'file': stored_image})
        if preprocess_response.status_code != 200:
            return jsonify({'error': 'Failed to preprocess image'}), 500
        preprocessed_image = preprocess_response.content

        # 3. Classify the image
        classify_response = requests.post(MODEL_SERVING_SERVICE_URL + '/classify', files={'file': preprocessed_image})
        if classify_response.status_code != 200:
            return jsonify({'error': 'Failed to classify image'}), 500

        return classify_response.json()

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/user/register', methods=['POST'])
def register_user():
    # Route the request to the User Management service
    return redirect(USER_MANAGEMENT_SERVICE_URL + '/register', code=307)

if __name__ == '__main__':
    app.run(port=5000)
