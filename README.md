# Malaria Cell Histopathology Classification - Deep Learning Project




<img src="https://github.com/Towet-Tum/Malaria-Cell-Histopathology-Classification-Transfer-Learning/raw/main/generated_malaria.png" alt="Alt Text" height="300" width="1000">


# Overview
This project aims to contribute to the fight against malaria in Africa through the application of deep learning techniques for the classification of malaria-infected and uninfected cells. Leveraging the power of transfer learning with VGG19, the model achieves an impressive accuracy of 94% and a validation score of 95%.

# Key Components
## Deep Learning Frameworks:

### TensorFlow: 
    Utilized for building and training the deep learning model.
### Keras: 
    Integrated with TensorFlow for efficient model construction.
## Transfer Learning:

### VGG19: 
    Implemented as a pre-trained model, the VGG19 architecture has been fine-tuned to expedite training and improve classification accuracy on the custom cell images dataset. The model was carefully tuned to adapt to the specific characteristics of the dataset, ensuring optimal performance in classifying malaria-parasitized and uninfected cells..
## Web Framework:

### Django: 
    Employed for developing a web-based platform to showcase and deploy the trained model.
## Machine Learning Operations (MlOps):

### MLflow: 
    Implemented for effective machine learning lifecycle management, including experimentation, reproducibility, and deployment.
### DVC (Data Version Control): 
    Integrated for efficient versioning and management of large datasets.
## Continuous Integration and Continuous Deployment (CI/CD):

### GitHub Actions: 
    Configured for automated CI/CD workflows, ensuring seamless integration and deployment processes.
### DVC: 
    Incorporated into CI/CD pipelines for versioned data and model management.
## Containerization:

### Docker: 
    Used for containerization of the application, providing a consistent and reproducible environment.
## Cloud Platform:

### Azure: 
    Selected as the cloud platform for hosting and scaling the application.
# Project Structure
### /src: 
    Contains the source code for the deep learning model.
### /mal-cell: 
    This is the virtual environment for the project.
### /logs: 
    Directory to store log files.
### /mlruns: 
    Captures MLflow experiments and metadata.
### /config: 
    Holds configuration files for the project.
### /generated_malaria.png: 
    Generated image from the project.
### /main.py: 
    Main Python script for the application.
### /MalariaClassificationApp: 
    Django web application directory.
### /research: 
    Directory for storing research-related files.
### /scores.json: 
    JSON file to store model evaluation scores.
### /params.yaml: 
    YAML file containing project parameters.
### /Dockerfile: 
    Docker configuration for containerizing the application.
### /dvc.yaml: 
    DVC configuration for tracking data versions.
### /LICENSE: 
    License file for the project.
### /README.md: 
    Project's README file containing documentation.
### /requirements.txt: 
    File specifying Python package dependencies.
### /setup.py: 
    Setup script for the project.
### /template.py: 
    Template script or placeholder for the project.
# Environment Setup:
## Clone the Repository:
    git clone https://github.com/Towet-Tum/Malaria-Cell-Histopathology-Classification-Transfer-Learning.git

## Install Dependencies:
    pip install -r requirements.txt
## Run the Application:
    MalariaClassification/python manage.py runserver

## Model Training:

    Utilize the web interface  for training the VGG19 model on the malaria dataset.
    Record experiments and metrics using MLflow.
## Continuous Integration/Continuous Deployment:

    Leverage GitHub Actions for automated testing and deployment.
## Containerization:

    Build the Docker image using the provided Dockerfile.
## Cloud Deployment (Azure):

    Deploy the Dockerized application on the Azure cloud platform for scalability.
    Contributing
    Contributions to this project are welcome. Please refer to the Contributing Guidelines for more details.

## License:
    This project is licensed under the MIT License - see the LICENSE.md file for details.

# Acknowledgments:
    The contributors and maintainers of TensorFlow, Keras, Django, MLflow, DVC, Docker, and Azure for their valuable tools and platforms.
    Organizations fighting against malaria for their impactful work.
    Together, let's contribute to the eradication of malaria and make a positive impact on global health.


