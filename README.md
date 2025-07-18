# Task Management API Service

## Overview
A robust FastAPI-based RESTful service for task management, designed as a foundation for DevOps and deployment practice scenarios. This project demonstrates modern Python web development practices and serves as a base for various deployment, containerization, and orchestration exercises.

## Features
- RESTful API endpoints for task management
- Async SQLite database integration
- Docker support
- Clean architecture with separation of concerns
- Type-safe API with Pydantic models
- OpenAPI (Swagger) documentation


## Project Structure
```text
├── router.py           # API routes and endpoints
├── repository.py       # Database operations
├── schemas.py          # Pydantic models
├── database.py         # Database configuration
├── main.py             # Application entry point
├── requirements.txt    # Project dependencies
└── Dockerfile          # Container configuration
```


## Technical Stack
- Python 3.13
- FastAPI - Modern web framework
- SQLAlchemy - SQL toolkit and ORM
- Pydantic - Data validation
- SQLite - Database
- Docker - Containerization

## Getting Started

### Prerequisites
- Python 3.13+
- virtualenv (recommended)
- Docker (optional)

### Local Development Setup

1. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
uvicorn main:app --reload
```


The API will be available at `http://localhost:8000`

### Docker Setup

1. Build the Docker image:
```bash
docker build -t task-management-api .
```

2. Run the container:
```bash
docker run -p 80:80 task-management-api
```

The API will be available at `http://localhost:80`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

### Available Endpoints

- `POST /tasks` - Create a new task
- `GET /tasks` - Retrieve all tasks

## DevOps Practice Scenarios

This project is designed to be used as a base for various DevOps and deployment scenarios:

- Containerization with Docker
- CI/CD pipeline setup
- Kubernetes deployment
- Infrastructure as Code (IaC)
- Monitoring and logging integration
- High availability setup
- Database migrations and scaling
- Security implementations

