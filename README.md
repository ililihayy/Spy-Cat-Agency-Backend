# Spy Cat Agency Backend

A simple API for managing cats, missions, and targets using FastAPI and SQLAlchemy.

## Getting Started

### Prerequisites
- Python 3.8+
- pip

### Installation

Clone the repository:
```bash
git clone https://github.com/ililihayy/Spy-Cat-Agency-Backend.git
cd Spy-Cat-Agency-Backend
```

Create and activate a virtual environment:
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
```

Install dependencies:
```bash
pip install -r requirements.txt
```

Run the server:
```bash
uvicorn app.main:app --reload
```

The API will be available at:
- API: http://127.0.0.1:8000
- Swagger docs: http://127.0.0.1:8000/docs
- Redoc: http://127.0.0.1:8000/redoc

## API Endpoints

### Cats

- `GET /cats/` – List all cats
- `GET /cats/{id}` – Get a single cat
- `POST /cats/` – Create a cat
- `PUT /cats/{id}` – Update a cat
- `DELETE /cats/{id}` – Delete a cat

### Missions

- `GET /missions/` – List all missions
- `GET /missions/{id}` – Get a single mission
- `POST /missions/` – Create a mission
- `PUT /missions/{id}` – Update a mission
- `DELETE /missions/{id}` – Delete a mission
- `POST /missions/{id}/assign_cat/{cat_id}` – Assign a cat to a mission

### Targets

- `GET /targets/` – List all targets
- `GET /targets/{id}` – Get a single target
- `POST /targets/` – Create a target
- `PUT /targets/{id}` – Update a target
- `DELETE /targets/{id}` – Delete a target

## Tech Stack

- **Framework**: FastAPI
- **ORM**: SQLAlchemy
- **Validation**: Pydantic
- **Database**: SQLite (default)
- **HTTP Client**: httpx (for TheCatAPI integration)

## Business Rules

- One cat can only have one mission at a time
- Each mission must have 1-3 targets
- Notes cannot be updated if target or mission is completed
- Missions cannot be deleted if assigned to a cat
- Cat breed must be validated against TheCatAPI
