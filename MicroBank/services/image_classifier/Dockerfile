# Use an official TensorFlow runtime as a parent image
FROM tensorflow/tensorflow:latest

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org flask

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Run classifier.py when the container launches
CMD ["python", "classifier.py"]
