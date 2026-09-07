# Movie Reviews

Full-stack application for managing movies, actors and movie reviews.
A full-stack web application for browsing movies, viewing their details and ratings, editing movie and actor information, and submitting reviews.

## Stack
The application was developed using Django REST Framework for the backend and Vue 3 for the frontend.

## Tech Stack

### Backend

- Python
- Django
- Django REST Framework
- PostgreSQL
- pytest
- pytest-django

### Frontend

- Vue 3
- Vite
- Vue Router
- Pinia
- Vuetify
- Axios
- Vitest
- Vue Test Utils

### Infrastructure

- Docker
- Docker Compose

## Features

The application provides the following functionality:

- Browse movies with pagination (5 movies per page)
- View movie details
- Display actors associated with a movie
- Display movie reviews
- Display the average movie rating
- Edit movie information
- Edit actor information
- Add reviews with a grade from 1 to 5
- Automatically update the average rating after adding a review
- Manage movies, actors, and reviews through Django Admin
- Handle movies without reviews
- Persist application data in PostgreSQL

No authentication is required, as specified by the assignment.


## Prerequisites

The easiest way to run the project is with Docker.

You need:

- Docker
- Docker Compose
- Git

No local Python, Node.js, or PostgreSQL installation is required when using Docker.

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd movie-reviews
```

Create the environment file:

```bash
cp .env.example .env
```

## Running the Application

Build and start all containers:

```bash
docker compose up -d --build
```

Apply database migrations:

```bash
docker compose exec backend python manage.py migrate
```

Load the initial dataset:

```bash
docker compose exec backend python manage.py loaddata initial_data
```

The fixture contains sample actors, movies, and reviews, including a movie without reviews to cover the empty-rating case.

Optionally create a Django administrator:

```bash
docker compose exec backend python manage.py createsuperuser
```


## Application URLs

Once the containers are running:

| Service | URL |
| --- | --- |
| Frontend | http://localhost:5173 |
| REST API | http://localhost:8000/api/movies/ |
| Django Admin | http://localhost:8000/admin/ |

## API Endpoints

### Movies

List movies:

```http
GET /api/movies/
```

The endpoint is paginated with 5 movies per page.

Example:

```http
GET /api/movies/?page=2
```

Retrieve a movie:

```http
GET /api/movies/{id}/
```

Update a movie:

```http
PATCH /api/movies/{id}/
```

Example:

```json
{
  "description": "Updated movie description"
}
```

Movie updates also support actor IDs where applicable:

```json
{
  "actors": [1, 2]
}
```

### Actors

Update an actor:

```http
PATCH /api/actors/{id}/
```

Example:

```json
{
  "first_name": "Leonardo",
  "last_name": "DiCaprio"
}
```

### Reviews

Create a review for a movie:

```http
POST /api/movies/{id}/reviews/
```

Example:

```json
{
  "grade": 5
}
```

Grades are validated by the backend and must be between 1 and 5.

## Django Admin

Django Admin can be accessed at:

```text
http://localhost:8000/admin/
```

It provides administration interfaces for:

- Movies
- Actors
- Reviews

Movies can also be managed together with their reviews through the configured admin interface.

## Backend Tests

Backend tests are written using pytest and pytest-django.

Run them with:

```bash
docker compose exec backend pytest -v
```

The backend test suite covers important application behavior including:

- Model relationships
- Movie listing
- Movie details
- Pagination
- Average rating calculation
- Movies without reviews
- Movie updates
- Actor updates
- Review creation
- Rating validation
- HTTP 404 behavior

## Frontend Tests

Frontend unit tests use Vitest and Vue Test Utils.

Run them with:

```bash
docker compose exec frontend npm run test:unit -- --run
```

The frontend tests focus on application behavior rather than testing Vuetify itself.

They cover:

- Movie card rendering
- Movies Pinia store
- API loading and error states
- Movie editing
- Actor editing
- Review creation
- Review validation
- Component events