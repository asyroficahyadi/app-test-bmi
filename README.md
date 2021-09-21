[![Test](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/workflows/Test/badge.svg)](https://github.com/asyroficahyadi/happyfresh-test-bmi/actions?query=workflow%3A%22Python+application%22++) [![Deploy](https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker/workflows/Deploy/badge.svg)](https://github.com/asyroficahyadi/happyfresh-test-bmi/actions/workflows/horusec-security-check.yml?query=workflow%3A%22Horusec+scanning+code%22++)

# HF BMI Calculator
  Calculator for Body Mass Index
  
## Prerequsites
Currenly supported and tested on Windows environment and supported to run on Docker Container.

Before use this apps, please install these prerequisites:
- python 3.9
- Docker Container

## Usage

### Local file
1. Clone the repository to your local machine
2. Install the requirements.txt

        python -r requirements.txt  

3. For running the apps on local web server, execute this command:

        uvicorn app.main:app 
        
4. From your web browser access the application using port 8000:

        localhost:8000
        
### Docker Container
1. Build Docker Image using this command:
 
        docker build -t app ./
        
2. From your web browser access the application using port 80:

        localhost:80        
        
        
### REST API
If you need REST API from this apps, you can use this method:

1. Add height in centimeter (cm) and weight in Kilogram (kg) value at the URL:

        http://localhost/ or http://127.0.0.1
 
2. Example of usage

        http://127.0.0.1/?height=170&weight=76

2. Example of Output:

        {
        "bmi":26.3,
        "label":"Overweight"
        }

### Build using Github Action
    This apps build using Github Action for every pull request in github.
    
 1. Copy the repository to your Github.
 2. You can create some branch and pull request (PR) to make the Github action workflows triggered to run.
 3. These workflow running after you add some pull request:
 
        - Python Application Workflow
          it will do unit test using pytest to check source code.
        
        - Horusec scanning code Workflow
          it will scanning the source code to check vulnerabilites on python.
       
 4. You can merge the branch and close the pull request to triggered the workflow to build docker images and it will deploy the application on Heroku. 
 

### Deploy on Heroku

If you want to review the REST this app in public. please check heroku deployment on this link:

Application: [https://bmi-happyfresh-docker.herokuapp.com/](https://bmi-happyfresh-docker.herokuapp.com/)

REST API: https://bmi-happyfresh-docker.herokuapp.com/?height=float&weight=float
Change height and weight for your input, example:  
[https://bmi-happyfresh-docker.herokuapp.com/?height=173&weight=76](https://bmi-happyfresh-docker.herokuapp.com/?height=173&weight=76)

        
