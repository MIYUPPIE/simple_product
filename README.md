# Business API

A Django REST API for managing product inventory with comprehensive error handling and standardized response formats.

## Features

- RESTful API endpoints for product management
- UUID-based product identification
- Standardized API response format
- Rate limiting and pagination
- CORS support
- Comprehensive error handling
- CI/CD pipeline with GitHub Actions

## Tech Stack

- Python 3.9+
- Django 5.1.7
- Django REST Framework 3.14.0
- SQLite (default database)

## Prerequisites

- Python 3.9 or higher
- pip (Python package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/business-api.git
cd business-api
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
cp .env.example .env
```
Edit `.env` file with your configuration.

5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

## API Documentation

### Products API (v1)

#### Endpoints

- `GET /api/v1/products/` - List all products (paginated)
- `POST /api/v1/products/` - Create a new product
- `GET /api/v1/products/{id}/` - Retrieve a product
- `PUT /api/v1/products/{id}/` - Update a product
- `DELETE /api/v1/products/{id}/` - Delete a product

#### Request/Response Formats

##### Product Object Schema
```json
{
    "id": "uuid",
    "name": "string",
    "category": "string",
    "price": "decimal",
    "stock_status": "string",
    "sku": "string",
    "description": "string",
    "created_at": "datetime",
    "updated_at": "datetime"
}
```

##### Success Response Format
```json
{
    "status": "success",
    "code": 200,
    "message": "Operation successful",
    "data": {
        "products": [
            {
                "id": "123e4567-e89b-12d3-a456-426614174000",
                "name": "Sample Product",
                // ... other product fields
            }
        ]
    }
}
```

##### Error Response Format
```json
{
    "status": "error",
    "code": 400,
    "message": "Operation failed",
    "errors": {
        "details": "Error description"
    }
}
```

#### Rate Limiting Headers
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1668144600
```

### API Implementation Details

The API is implemented in `products/views.py` using Django REST Framework's `ModelViewSet`. Key features include:

#### Error Handling
- Comprehensive try-catch blocks for all operations
- Standardized error responses
- Proper HTTP status codes

#### Rate Limiting
- Anonymous users: 100 requests per minute
- Rate limit headers included in responses

#### Pagination
- Default page size: 10 items
- Maximum page size: 100 items
- Configurable via `page_size` query parameter

## Development

### Running Tests
```bash
python manage.py test
```

### Code Coverage
```bash
coverage run manage.py test
coverage report
```

### Linting
```bash
flake8
```

## CI/CD

The project uses GitHub Actions for:
- Running tests on Python 3.9, 3.10, and 3.11
- Code linting
- Security checks
- Automated deployment (when configured)

## Security

- CORS configuration required for frontend access
- Rate limiting enabled
- Environment variables for sensitive data
- Security middleware enabled

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| DJANGO_SECRET_KEY | Django secret key | Required |
| DJANGO_DEBUG | Debug mode | False |
| DJANGO_ALLOWED_HOSTS | Allowed hosts | Required |
| CORS_ALLOWED_ORIGINS | CORS origins | Required |

## Project Structure

```
business-api/
├── business_api/        # Project configuration
├── products/           # Products app
│   ├── views.py       # API views and logic
│   ├── models.py      # Product model
│   ├── serializers.py # API serializers
│   └── urls.py        # API routing
├── .env               # Environment variables
├── .env.example       # Environment template
└── manage.py          # Django management
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

### Coding Standards

- Follow PEP 8 guidelines
- Include docstrings for all functions
- Write unit tests for new features
- Maintain consistent error handling
- Update documentation for API changes

## License

[MIT License](LICENSE)

## Support

For support, please open an issue in the GitHub repository.
