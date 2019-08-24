## APP Pipenv

A simple *Flask* application "Hello, Earth!" using `Pipenv` and `Python 3.7.4`.

#### Cloning this repo
 
 `git clone git@github.com:mariahsonja/app_pipenv.git`
 
#### Installing Pre-requisites

`pipenv install --dev`
 
#### Running locally

`pipenv install` 

For a new virtual environment: `pipenv shell`

For a development server: `FLASK_APP=app flask run`

#### Building and running the Docker image

`docker build -t app_pipenv-app .`

`docker run -p 8000:8000 app_pipenv-app`

#### Referencies

For more details on Pipenv: https://github.com/pypa/pipenv


**Thank you!**
