# FastAPI Employee Management App

This project is a simple employee management application built with FastAPI, SQLAlchemy, and PostgreSQL. It provides a RESTful API for managing employee records and includes a basic web interface.

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

## API Documentation

FastAPI provides automatic API documentation. You can access it by navigating to:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Project Structure

```
.
├── alembic/
│   └── versions/
├── app/
│   ├── models/
│   ├── routes/
│   ├── static/
│   ├── templates/
│   ├── database.py
│   └── main.py
├── .env
├── .gitignore
├── alembic.ini
├── README.md
└── requirements.txt
```

## Development

To add new features or modify existing ones:

1. Create a new branch:
   ```
   git checkout -b feature-branch-name
   ```

2. Make your changes and commit them:
   ```
   git add .
   git commit -m "Description of changes"
   ```

3. Push your changes and create a pull request:
   ```
   git push origin feature-branch-name
   ```

## Testing

(Note: Add information about running tests once you've set up a testing framework)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
