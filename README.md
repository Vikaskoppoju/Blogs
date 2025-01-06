# Multi-Service Blog Platform

This project demonstrates the creation, containerization, orchestration, and deployment of a multi-service blog platform using Docker containers and AWS. The platform includes a User Service, Blog Service, Comment Service, and a PostgreSQL Database Service, each running in its own container.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Services Overview](#services-overview)
3. [Dockerization](#dockerization)
4. [Service Orchestration](#service-orchestration)
5. [AWS Deployment](#aws-deployment)
6. [Environment Management](#environment-management)
7. [Running the Project Locally](#running-the-project-locally)
8. [Deploying to AWS](#deploying-to-aws)
9. [API Endpoints](#api-endpoints)
10. [Testing the API with Postman](#testing-the-api-with-postman)
11. [Live Deployment](#live-deployment)
12. [Documentation](#documentation)
13. [License](#license)

## Project Overview

The project consists of four main services:

- **User Service**: Handles user authentication, registration, and profile management.
- **Blog Service**: Manages blog posts and supports pagination for scalability.
- **Comment Service**: Allows users to comment on blog posts.
- **Database Service**: Uses PostgreSQL to store data for all services.

The services are containerized using Docker, orchestrated using Docker Compose, and deployed on AWS EC2.

## Services Overview

### User Service

- Manages user authentication (JWT) and profile management.
- Passwords are securely stored using bcrypt hashing.

**Exposed Endpoints**:
- `POST /register/`: Register a new user.
- `POST /login/`: Authenticate a user.
- `GET /users/<id>`: Retrieve user details.
- `PUT /users/<id>`: Update user details.
- `DELETE /users/<id>`: Delete user account.

### Blog Service

- Manages blog posts.
- Supports pagination for listing blog posts.

**Exposed Endpoints**:
- `POST /blogs/`: Create a new blog post.
- `GET /blogs/`: List all blog posts.
- `GET /blogs/<id>`: Fetch a specific blog post.
- `PUT /blogs/<id>`: Edit an existing blog post.
- `DELETE /blogs/<id>`: Delete a specific blog post.

### Comment Service

- Handles comments for blog posts (flat structure, with the option to expand for nested comments).

**Exposed Endpoints**:
- `POST /comments/`: Add a comment to a blog post.
- `GET /comments?post_id=<id>`: List comments for a specific blog post.

### Database Service

- PostgreSQL database for storing data for all services, each using its own schema.

## Dockerization

Each service is containerized using Docker. A Dockerfile is provided for each service to create the Docker image.

- **User Service Dockerfile**: Defines the setup for the User service.
- **Blog Service Dockerfile**: Defines the setup for the Blog service.
- **Comment Service Dockerfile**: Defines the setup for the Comment service.

The Dockerfiles use multi-stage builds to reduce image size and improve build efficiency.

## Service Orchestration

The services are orchestrated using Docker Compose. The `docker-compose.yml` file defines all the services, including:

- **Web Services**: User, Blog, Comment.
- **Database Service**: PostgreSQL.

The Compose file ensures that the services communicate with each other over a shared network and that the data is persisted using volumes.

## AWS Deployment

Deploy the multi-service application on AWS using an EC2 instance.

### AWS Resources Used:
- **EC2 instance**: For running the Docker containers.
- **RDS**: For PostgreSQL database management (optional if using EC2 PostgreSQL).

### Steps for deployment:
1. **Set up EC2**: Launch an EC2 instance and SSH into it.
2. **Install Docker**: Set up Docker and Docker Compose on the EC2 instance.
3. **Transfer Files**: Use SCP to transfer project files to EC2.
4. **Build and Run Containers**: Build the Docker containers using Docker Compose and run the application.

## Environment Management

Use `.env` files for managing environment variables like database credentials. Separate `.env` files are provided for local development and production environments.

### Example `.env` file for development:
```env
DEBUG=True
SECRET_KEY=your-secret-key
DB_HOST=db
DB_PORT=5432
DB_NAME=blogdb
DB_USER=admin
DB_PASSWORD=password
