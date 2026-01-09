# MLOps Homework 2: Implementing CI/CD Pipeline

This project implements an automated MLOps pipeline for a High-Cardinality Prediction Service. It demonstrates the transition from manual workflows to automated CI/CD processes, ensuring code quality, integration stability, and deployment reliability.

# Project Overview

The primary goal is to establish a Continuous Integration (CI) and Continuous Deployment (CD) backbone that prevents defective code or models from reaching production environments.

# Technical Specifications

CI/CD Platform: GitHub Actions
Programming Language: Python 3.10
API Framework: FastAPI
Testing Framework: Pytest
Static Analysis: Flake8
Containerization: Docker

# Pipeline Architecture

Part 1: The Commit Stage (Continuous Integration)
This stage triggers on every push and pull request to verify code integrity:
Automated Unit Testing: Implements tests for the feature engineering (hashing) logic to ensure correct bucket indexing for high-cardinality features.
Code Analysis/Linting: Uses Flake8 to enforce PEP 8 standards. The pipeline is configured to fail if code style or syntax errors are detected.

# Part 2: The Automated Acceptance Gate (Continuous Deployment)

This stage ensures the system works as a whole before being considered ready for deployment:
Component Testing: Verifies the interaction between the FastAPI serving logic and the hashing functions.
Build & Package: Packages the code and its dependencies into a single Docker image to ensure consistency across environments.
Smoke Testing: Spins up the container and executes a health-check script to verify the service is responding with a 200 OK status.

# Part 3: "Stop the Line" Simulation

To demonstrate the safety mechanisms of the pipeline:
A logic bug was intentionally introduced into the feature engineering code.
The pipeline successfully detected the failure during the Unit Test stage.
Result: The deployment process was blocked, preventing the build of a faulty Docker image and showcasing the "Stop the Line" principle.

# Repository Structure

.github/workflows/ci-cd.yml: Pipeline configuration.
app/: Application source code (main.py, features.py).
tests/: Test suites (unit, component, and smoke tests).
Dockerfile: Instructions for building the container image.
requirements.txt: Python dependencies.

# Execution Instructions

Local TestingTo run the automated tests locally:
Install dependencies: pip install -r requirements.txt
Set PYTHONPATH: export PYTHONPATH=$PYTHONPATH:$(pwd)
Run tests: python -m pytest

# Local Deployment

To build and run the service via Docker:
Build image: docker build -t mlops-service .
Run container: docker run -p 8000:8000 mlops-service
