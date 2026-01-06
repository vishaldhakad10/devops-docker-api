# DevOps Docker FastAPI Project

## Project Overview

This project is a containerized backend API built using FastAPI and Docker.
It demonstrates how a backend service can be packaged into a Docker container
and run consistently across different environments following DevOps fundamentals.

The project focuses on API development, containerization, and service health monitoring.

---

## Features

- FastAPI REST API
- Swagger UI for live API testing
- Dockerized application
- Health check endpoint

---

## Project Structure

```text
devops-docker-api/
├── app/
│   └── main.py        # FastAPI application entry point
├── Dockerfile         # Docker image configuration
├── requirements.txt  # Python dependencies
├── README.md          # Project documentation


---

## Run Locally using Docker

```bash
docker build -t devops-api .
docker run -p 8000:8000 devops-api

## API Endpoints

| Method | Endpoint   | Description                  |
|--------|------------|------------------------------|
| GET    | `/`        | Root endpoint                |
| GET    | `/health`  | Health check for the service |


## DevOps Skills Demonstrated

- Docker image creation using Dockerfile
- Container lifecycle management (build, run, stop)
- Port mapping and service exposure
- REST API development with FastAPI
- Swagger / OpenAPI documentation
- Health check endpoint for monitoring
- Git & GitHub version control



