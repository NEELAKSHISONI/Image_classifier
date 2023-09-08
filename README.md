# Image_classifier

1. python -v  #check python version
2. if you are on windows 10 , create you own virtual environment
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
   
