  SWE40006 – Software Deployment and Evolution
 Deployment Task 4 – Docker Containerisation Portfolio

Student: Isara Erandi  
Unit: SWE40006 – Software Deployment and Evolution  
Assessment: Deployment Task 4  
Target Level: High Distinction – Task 4.4  
Semester: Semester 2, 2026  

---

 Project Overview

This repository contains the source code, Dockerfiles, configuration files, and supporting application files developed for Deployment Task 4.

The portfolio demonstrates the use of Docker for application containerisation and deployment. The implementation progresses through the assessment levels from basic Docker installation and verification to custom application containerisation, Docker Hub deployment, secondary-host testing, runtime configuration, and a non-web command-line application with persistent storage.

---

 Task 4.1 – Docker Setup and Verification

The first stage involved setting up the Docker environment and verifying that Docker was functioning correctly.

The implementation included:

- Docker Desktop installation and configuration
- Docker CLI verification
- Docker Hub account configuration
- Pulling the standard `hello-world` Docker image
- Running the `hello-world` container successfully
- Verifying containers and images using Docker CLI commands

This established a working Docker environment for the remaining deployment tasks.

---

 Task 4.2 – Python Application Containerisation

A Python application was prepared and containerised using Docker.

This stage demonstrates:

- Python application development
- Runtime dependency configuration
- Dockerfile creation
- Docker image building
- Container execution
- Docker Hub image publishing
- Pulling and running the image through a second Docker/WSL environment

The application image was published to Docker Hub to demonstrate image portability and deployment.

---

 Task 4.3 – Custom Web Application

A custom Flask-based web application named Isara Task Manager was developed and deployed as a Docker container.

The application provides a simple task-management interface and demonstrates a containerised web workload.

Key implementation features include:

- Flask web application
- Custom Dockerfile
- Python dependency management
- Container port exposure
- Host-to-container port mapping
- Runtime environment variables
- Health-check endpoint
- Docker image versioning
- Docker Hub deployment
- Container execution and verification

The application listens on port `5000` inside the container and was tested through mapped host ports.

Example:

```bash
docker run -d --name isara-task-manager-v2 -p 8082:5000 isara-task-manager:2.0
