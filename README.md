# Microservices Template

This repository contains a microservices template with the following components:

- **API Gateway**: Apache APISIX
- **Service Registry**: Kubernetes Service
- **Inter-microservice communication**: Kafka, REST API
- **Services**: Spring Boot (Java)

## Getting Started

1. Clone the repository
2. Navigate to the directory.
3. Ensure Docker and Docker Compose are installed.
4. Build and run the services:
   ```sh
   docker-compose up --build
   ```

## Services
- User Service: Provides user management functionality.

## API Endpoints
- `/users`: Retrieve a list of users.

## License
MIT