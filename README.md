# ICARGO MACHINE LEARNING PROJECT
## Project Title: 
    Cargo Screening Certification Predictor
## Description:
The Cargo Screening Certification Predictor is a machine learning project designed to assist cargo screening organizations in identifying individuals who are likely to pass the final certification exam with a score of 85% or higher. The project leverages a dataset containing training assessment test scores, HR initial recruitment exam scores, and a variety of demographic features to make predictions.

## Background:
In the context of cargo screening, ensuring that individuals meet the required certification standards is crucial for maintaining the security and efficiency of cargo operations. The final certification exam serves as a critical benchmark for assessing an individual's readiness and competence in this field.
### Dataset:
 The project uses a comprehensive dataset that includes the following key features:

Training Assessment Test Scores: Scores obtained by individuals in post-training assessments, which evaluate their understanding of cargo screening procedures and principles.

HR Initial Recruitment Exam Score: The score achieved by candidates in the HR initial recruitment exam, which measures their baseline aptitude and knowledge.

Demographic Features: Additional demographic information about each candidate, such as age, gender, educational background, and work experience.
## Objective:
The primary objective of this project is to build a machine learning model capable of predicting whether a candidate is likely to pass the final certification exam with a score of at least 85%. By doing so, cargo screening organizations can proactively identify individuals who may require additional training or support to meet the certification criteria.
## Methodology:
 The project follows these key steps:

Data Preprocessing: The dataset is cleaned, missing values are handled, and categorical features are encoded appropriately.

Feature Selection: Relevant features are selected, and feature engineering may be performed to create new informative features.

Model Building: Various machine learning algorithms, such as logistic regression, decision trees, random forests, and neural networks, are trained and evaluated on the dataset.

Model Evaluation: Model performance is assessed using metrics like accuracy, precision, recall, and F1-score, with a focus on achieving high accuracy and recall for identifying potential candidates.

Deployment: The best-performing model is deployed as a prediction tool for cargo screening organizations to assess candidates' likelihood of passing the final certification exam.
## Benefits:

The Cargo Screening Certification Predictor offers several benefits, including:

Improved efficiency in identifying candidates likely to succeed in the final certification exam.
Reduced training costs by targeting resources on individuals who need additional support.
Enhanced security and competence in cargo screening operations.

## Technology Stack:

Programming Language:
     Python 3.9
Machine Learning Frameworks:
     pandas,numpy,seaborn,matplotlib,scikit-learn,catboost,xgboost
Web Interface: 
    Flask (for a user-friendly web interface)
Database: 
    MSSQL (for storing screening data)
Deployment:
    Azure- Container Registery and WebApp for containerization and orchestration.
 

## Disclaimer:
This project is intended for demonstration purposes and as a proof-of-concept for cargo screening certification automation. It is not intended for real-world cargo security applications without appropriate validation and certification.

## Azure WebApp Deploy't- icargoaz
steps:
1. create Az Container registery (icargoaz)and save 
	- Login server= icargoaz.azurecr.io
	- UN= icargoaz
	- pw= 3qxBheNN4deq9dH7Y6q9h3mDKvjuCFvlcb8ClFvHPQ+ACRAX5ktm
2. Docker set up in local and push container registery
	- docker build -t icargoaz.azurecr.io/icargoaz:latest .
	- docker login icargoaz.azurecr.io ==> use the above un and pw in (1)
	- docker push icargoaz.azurecr.io/icargoaz:latest
3. create Az webapp with the container and use the image built in (2)
	
4. conf github deploy't center
	once webapp is created, go to Deployment center tab of the webapp and turn on continuous deploy't radio btn, choose Github Actions:... radio btn ...
	save the conf and go to Github Actions tab to see the deploy't progress
