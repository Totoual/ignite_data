# Ignite Data Assessment.

This is an assessment.

## Table of Contents

- [Ignite Data Assessment](#ignite-data)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Running Linters](#running-linters)
  - [Running Tests](#running-tests)
  - [API Endpoints](#api-endpoints)

## Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Poetry](https://python-poetry.org/docs/#installation)

## Installation

1. **Clone the repository**:

    ```bash
    git clone git@github.com:Totoual/ignite_data.git
    cd ignite_data
    ```

2. **Install dependencies** using Poetry:

    ```bash
    poetry install
    ```

3. **Activate the Poetry environment**:

    - On Unix-based systems (Linux/macOS):

      ```bash
      source $(poetry env info --path)/bin/activate
      ```

4. **Setup environment variables**:


    You can update the env variables or overwritte them in config folder.

## Usage

1. **Run the API**:

    ```bash
    poetry run api
    ```

2**API Documentation**:

    Access the interactive API documentation at `http://localhost:8000/docs`.

## Running Linters

1. **Run Linter** using Black:

    ```bash
        poetry run black assessment/
    ```

2. **Run TypeCheck** using mypy:
   
    ```bash
        poetry run mypy assessment/
    ``` 

## Running Tests

1. **Run tests** using Pytest:

    ```bash
     poetry run pytest --cov --cov-branch --cov-report=html tests/
    ```

## API Endpoints

List and describe the available API endpoints here.

For example:

- `GET /medication-request`: Retrieve medication requests with optional filters.
- `POST /medication-request`: Create a new medication request.
- `PATCH /medication-request/{medication_request_id}`: Update a medication request.


## Assumptions

- Clinician registration_id as a UUID and primary key in the db (Thought it will be unique)
- Medication id is an auto increment field

You will need to create a clinician, a patient and a medication in the db in-order to create a new
medication request. These endpoints are not provided.
