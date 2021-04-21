# react-fastapi-starter
Quickstart for building a React-FastAPI Web-Application

## Installation

### Set Environment Variables
Duplicate the `.env.template` file and rename it to `.env`.
    
    cp backend/.env.template backend/.env
Change the variable values accordingly.

### Build Docker Container
    docker-compose up -d --build

### Run Database Migration
    docker-compose exec server bash
    alembic upgrade head

## Development

### Create Database Migration
    docker-compose exec server bash
    alembic revision -m "migration message"

### Interact with Database
    docker-compose exec db psql -h localhost -U postgres --dbname=postgres

## References
The React-FastAPI Starter Project is inspired by [Jeff Astor](https://www.jeffastor.com/blog/up-and-running-with-fastapi-and-docker)