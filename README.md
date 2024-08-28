
<p align="center">
  <a href="https://www.withcoherence.com">
    <img alt="Coherence Logo" title="Coherence" src="./logo.png" width="400" style="color: black">
  </a>
</p>


<p align="center">
  <i>Platform-as-a-service in your own Cloud</i><br/> 
  <a href="https://www.withcoherence.com">withcoherence.com</a>
</p>

<h1 align="center">
FastAPI and Postgres Example
</h1>

<p align="center">
<img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi">
<img src="https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white">
</p>

<br/>

# Full stack FastAPI and Postgres application (employee management)

<p>
This is the code to accompany the tutorial available at our <a href="https://docs.withcoherence.com/coherence-templates/full-stack-template/?tabs=fastapi">Framework Guide (FastAPI)</a> page.
</p>

You can use it as a starting point for any full stack FastAPI application. Read the guide to see how to deploy it to a production environment in your own cloud, or see the instructions below to run a development version of it locally.

## Getting Started 

Fork the repository to your GitHub account. To test locally, clone the forked repository to your machine. You will need to have Docker installed.

## Prerequisites

Before you begin, ensure you have the following installed on your system:
- Python 3.8+
- PostgreSQL
- pip (Python package manager)

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/fastapi-employee-app.git
   cd fastapi-employee-app
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Create a PostgreSQL database for the project:
   ```
   createdb employee_app
   ```

5. Create a `.env` file in the root directory with the following content:
   ```
   DB_USER=your_postgres_username
   DB_PASSWORD=your_postgres_password
   DB_HOST=localhost
   DB_NAME=employee_app
   ```
   Replace `your_postgres_username` and `your_postgres_password` with your actual PostgreSQL credentials.

6. Run the database migrations:
   ```
   alembic upgrade head
   ```

## Running the Application

1. Start the FastAPI server:
   ```
   uvicorn app.main:app --reload
   ```

2. Open your web browser and navigate to `http://localhost:8000` to access the application.

## Resources

Take a look at the following for more information:

* [Coherence](https://www.withcoherence.com)
* [Why Choose Coherence](https://docs.withcoherence.com/#why-choose-coherence)
* [Coherence Documentation](docs.withcoherence.com)

**Cloud Infrastructure On Autopilot**

_Deploy containerized and serverless apps to your own cloud in minutes, not weeks._
