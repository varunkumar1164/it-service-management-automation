# IT Service Management & Helpdesk Automation System

## Overview

A web-based IT helpdesk application for creating, tracking,
updating, and resolving technical support tickets.

The application is built using Python Flask and deployed
using Docker and Kubernetes on an AWS EC2 Ubuntu server.

## Features

- Create support tickets
- Assign ticket priorities
- View all tickets
- Search tickets
- Update ticket status
- Delete tickets
- Deploy multiple application replicas

## Technology Stack

- Python
- Flask
- HTML and CSS
- AWS EC2
- Ubuntu Linux
- Docker
- Kubernetes
- Minikube
- kubectl
- Git and GitHub

## Architecture

User Browser
    |
    v
AWS EC2 - Ubuntu
    |
    v
Docker Image
    |
    v
Minikube / Kubernetes
    |
    v
Kubernetes Service
    |
    v
Flask Helpdesk Application

## Project Structure

    it-helpdesk-automation/
    ├── app.py
    ├── requirements.txt
    ├── Dockerfile
    ├── .dockerignore
    ├── .gitignore
    ├── README.md
    ├── templates/
    │   ├── index.html
    │   └── dashboard.html
    └── kubernetes/
        ├── deployment.yaml
        └── service.yaml

## Run Locally

Create a virtual environment:

    python3 -m venv .venv

Activate it on Linux:

    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

Start the application:

    python app.py

Open:

    http://localhost:5000

## Build Docker Image

    docker build -t helpdesk-app:v1 .

## Run Docker Container

    docker run --rm -p 5000:5000 helpdesk-app:v1

## Deploy on Minikube

Start Minikube:

    minikube start --driver=docker

Load the image:

    minikube image load helpdesk-app:v1

Apply Kubernetes resources:

    kubectl apply -f kubernetes/deployment.yaml
    kubectl apply -f kubernetes/service.yaml

Check the deployment:

    kubectl get deployments
    kubectl get pods
    kubectl get services

Access the application:

    kubectl port-forward service/helpdesk-service 8080:5000

Open:

    http://localhost:8080

## Current Limitations

Tickets are stored in application memory and are not persistent.
Data is not shared across replicas.

A database such as MySQL is required for persistent ticket storage
and consistent data across application replicas.

## Future Enhancements

- Integrate MySQL for persistent storage
- Implement user authentication and role-based access
- Automate Docker builds with Jenkins
- Store images in Amazon ECR
- Provision AWS infrastructure using Terraform
- Add application monitoring using Prometheus and Grafana