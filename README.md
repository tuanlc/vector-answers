# Vector Answers

A project for vector-based question answering.

**Note: The following guidance should be executed under the `./server` folder.**

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd vector-answers
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
cp .env.example .env
```

4. Configure your environment variables in the `.env` file as needed.

## Database Setup

5. Start the database instance using Docker Compose:
```bash
docker-compose up -d
```

6. Verify the database is running:
```bash
docker-compose ps
```

To stop the database when done:
```bash
docker-compose down
```

## Running the Application

7. Start the application server using uvicorn:
```bash
uvicorn main:app --reload
```

8. Access the application at `http://localhost:8000`

For production deployment, use:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```