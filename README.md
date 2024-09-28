# Inventory Management System API

## Overview

This project is a backend API for an Inventory Management System developed using Django Rest Framework (DRF) and JWT (JSON Web Token) based authentication. The system allows authenticated users to perform CRUD operations (Create, Read, Update, Delete) on inventory items, integrates caching with Redis, and utilizes PostgreSQL as the primary database.

## Features

- JWT Authentication for secure access to API endpoints.
- CRUD operations on inventory items.
- Caching with Redis for improved performance.
- PostgreSQL database for storing inventory items.
- Comprehensive error handling and logging.
- Unit tests for all endpoints to ensure reliability.

## Prerequisites

Before setting up the project, ensure that you have the following software installed:

- Python 3.8+
- PostgreSQL
- Redis
- Django 4.0+
- Django Rest Framework
- djangorestframework-simplejwt
- psycopg2

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd inventory_management
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

### 4. Configure Database

1. Create a new PostgreSQL database:

   ```sql
   CREATE DATABASE inventory_db;
   ```

2. Create a PostgreSQL user and grant privileges:

   ```sql
   CREATE USER inventory_user WITH PASSWORD 'your_password';
   GRANT ALL PRIVILEGES ON DATABASE inventory_db TO inventory_user;
   ```

3. Configure your database settings in `inventory_system/settings.py`:

   ```python
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'inventory_db',
           'USER': 'inventory_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

### 5. Configure Redis

Ensure that Redis is installed and running on your local machine. Update the `CACHES` configuration in `inventory_system/settings.py` if necessary.

```python
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}
```

### 6. Apply Migrations and Create a Superuser

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

### 8. Access the Application

- **Admin Panel**: `http://127.0.0.1:8000/admin`
- **API Endpoints**: `http://127.0.0.1:8000/api/`

## API Documentation

### Authentication

1. **User Registration**

   - **Endpoint**: `POST /api/register/`
   - **Request Body**:

     ```json
     {
         "username": "your_username",
         "password": "your_password",
         "email": "your_email@example.com"
     }
     ```

   - **Response**:

     ```json
     {
         "id": 1,
         "username": "your_username",
         "email": "your_email@example.com"
     }
     ```

2. **User Login (Obtain JWT Token)**

   - **Endpoint**: `POST /api/token/`
   - **Request Body**:

     ```json
     {
         "username": "your_username",
         "password": "your_password"
     }
     ```

   - **Response**:

     ```json
     {
         "refresh": "refresh_token_here",
         "access": "access_token_here"
     }
     ```

3. **Token Refresh**

   - **Endpoint**: `POST /api/token/refresh/`
   - **Request Body**:

     ```json
     {
         "refresh": "refresh_token_here"
     }
     ```

   - **Response**:

     ```json
     {
         "access": "new_access_token_here"
     }
     ```

### Inventory Management

1. **Create an Inventory Item**

   - **Endpoint**: `POST /api/items/`
   - **Headers**: `Authorization: Bearer <access_token>`
   - **Request Body**:

     ```json
     {
         "name": "Item Name",
         "description": "Item Description",
         "quantity": 100,
         "price": 50.0
     }
     ```

   - **Response**:

     ```json
     {
         "id": 1,
         "name": "Item Name",
         "description": "Item Description",
         "quantity": 100,
         "price": 50.0,
         "created_at": "2024-09-28T10:00:00Z",
         "updated_at": "2024-09-28T10:00:00Z"
     }
     ```

2. **Read an Inventory Item**

   - **Endpoint**: `GET /api/items/{item_id}/`
   - **Headers**: `Authorization: Bearer <access_token>`
   - **Response**:

     ```json
     {
         "id": 1,
         "name": "Item Name",
         "description": "Item Description",
         "quantity": 100,
         "price": 50.0,
         "created_at": "2024-09-28T10:00:00Z",
         "updated_at": "2024-09-28T10:00:00Z"
     }
     ```

3. **Update an Inventory Item**

   - **Endpoint**: `PUT /api/items/{item_id}/`
   - **Headers**: `Authorization: Bearer <access_token>`
   - **Request Body**:

     ```json
     {
         "name": "Updated Item Name",
         "description": "Updated Item Description",
         "quantity": 150,
         "price": 75.0
     }
     ```

   - **Response**:

     ```json
     {
         "id": 1,
         "name": "Updated Item Name",
         "description": "Updated Item Description",
         "quantity": 150,
         "price": 75.0,
         "created_at": "2024-09-28T10:00:00Z",
         "updated_at": "2024-09-28T11:00:00Z"
     }
     ```

4. **Delete an Inventory Item**

   - **Endpoint**: `DELETE /api/items/{item_id}/`
   - **Headers**: `Authorization: Bearer <access_token>`
   - **Response**:

     ```json
     {
         "message": "Item deleted successfully."
     }
     ```

## Running Unit Tests

To run the unit tests for all API endpoints, use the following command:

```bash
python manage.py test
```

This will execute all unit tests defined in the `tests.py` file for your API.

## Logging

The application integrates logging for tracking API usage, errors, and other significant events. By default, logs are stored in a file named `inventory_system.log` located in the project root directory.

You can configure the logging settings in `settings.py`:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'inventory_system.log',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For any questions or issues, please reach out to [sandeepsahu1215@gmail.com].
