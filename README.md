### APP Pipenv

A simple *Flask* application "Hello, Earth!" using Pipenv.

#### Cloning this repo
 
 `git clone ......`
 
#### Installing Pre-requisites

`pipenv install --dev`
 
#### Running locally

`pipenv install` 

For a new virtual environment: `pipenv shell`

For a development server: `FLASK_APP=app flask run`

#### Building and running the Docker image

`docker build -t app_pipenv-app .`

`docker run -p 8000:8000 app_pipenv-app`


**Thank you!**
