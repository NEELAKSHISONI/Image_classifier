# Image_classifier

1. python -v  #check python version
2. # Image Classifier Project

This project demonstrates how to create a Python environment, install TensorFlow, build a Docker image, and run a Docker container for image classification.

## Prerequisites

- Windows 10
- Docker Desktop
- [Python](https://www.python.org/downloads/) installed
- [Virtualenv](https://pypi.org/project/virtualenv/) installed
- [TensorFlow](https://www.tensorflow.org/install) installed in the virtual environment

## Getting Started

### Create a Virtual Environment

Open a command prompt or terminal and navigate to your project directory.

```shell
# Install virtualenv
pip install virtualenv

# Create the virtual environment
virtualenv env

# Activate the environment

Windows Powershell:
.\env\Scripts\activate

Unix with Bash or zsh:
source env/bin/activate
# Install TensorFlow in the virtual environment
pip install tensorflow
# Build the Docker image
docker build -t image_classifier .
# Run the Docker container
docker run -p 5000:5000 image_classifier
Use Postman or any HTTP client to make a POST request to: http://127.0.0.1:5000/predict
3. if you are on windows 10 , create you own virtual environment
   #code . in command prompt 
    cd <your project path>

  Install virtualenv

  pip install virtualenv

  #Create the virtual environment

  virtualenv <envname>

  #Activate the env

  Windows Powershell: .\<envname>\Scripts\activate
  Unix with Bash or zsh: source <envname>/bin/activate
  Then now you install tensorflow

  (<envname>) $ pip install tensorflow
3. Build the Docker image using the Dockerfile (docker desktop ) .
   docker build -t image_classifier .
4.  Run the Docker container .
    docker run -p 5000:5000 image_classifier
5. send images to the /predict endpoint to get predictions.
    http://127.0.0.1:5000/
    on postman --> u can post http://127.0.0.1:5000/predict
   
