# ML_Model_DJango_CF
Deploy ML model using Django on Cloud Foundry

# Django Demo App
This is a basic Django project created for demonstration purposes. The project includes a simple Django app with a single view that takes multiple parameters like glucose, Blood Pressure and BMI and predicts Diabetes. And deploy that on cloud foundry.

## Requirements
Python 3.x

Django 5.x

## Installation
1. Clone this repository to your local machine:
   
```git clone https://github.com/your_username/django-demo-app.git```

2. Navigate to the project directory:
   
```cd django-demo-app```

3. Create a virtual environment:

```python3 -m venv venv```

4. Activate the virtual environment:
  * On macOS and Linux:
    ```source venv/bin/activate```
  * On Windows (cmd):
    ```venv\Scripts\activateOn``` 
  * Windows (PowerShell):
    ```.\venv\Scripts\Activate.ps1```

## Install dependencies:

```pip install -r requirements.txt```

## Local Development 
* Run the Django development server:
```python manage.py runserver```

* Open your web browser and navigate to ```http://localhost:8000``` to view the application.

## Deployment to Cloud Foundry
1. Install the Cloud Foundry CLI if you haven't already: Cloud Foundry CLI Installation Guide
2. Log in to your Cloud Foundry account: 
```cf login -a <API_ENDPOINT> -u <USERNAME> -p <PASSWORD>```

4. Navigate to the directory of your Django project where manifest.yml file is present.
5. Deploy your application to Cloud Foundry:
```cf push```

6. Access your deployed application using the provided URL.

## Configuration
* *settings.py* : Modify Django settings as needed for your project.
* *manifest.yml* : Update Cloud Foundry deployment configuration (e.g., application name, memory allocation, etc.).

## Contributing 
Contributions are welcome! Feel free to open an issue or submit a pull request for any improvements or features you'd like to see.
