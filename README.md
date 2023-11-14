
[![Python application test with Github Actions](https://github.com/ChakreshIITGN/MLOps_python_func/actions/workflows/main.yml/badge.svg)](https://github.com/ChakreshIITGN/MLOps_python_func/actions/workflows/main.yml)

# MLOps_python_func
This repository is part of an exercise to understand the CI/CD using python and github actions 


### Using Google Colab - 

> If you create a link to the google colab notebook into your repository you will have to update it manually everytime you make changes to the notebook - ?

### Using Github Codespaces - 
> Create a codespace for the github repo - this is a good practice in MLOps
> Then the first thing to do is create a virtual environment and source it in the bashrc using the following commands
    ` python -m venv <vname> || source <vname>/bin/activate`
> This is good since it will be easy to maintain and install dependencies for python

## Creating a Scaffold


### Runnning the Post request 
`curl -X 'POST' \
  'https://sturdy-space-journey-7rrqv779v9rcxr66-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Microsoft",
    "length": 3
    }'`


### Building an image - 

    `docker build .`
    `docker image -ls`

to run  - `docker run -p 127.0.0.1:8080:8080 <imageID>`

