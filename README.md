# Business API

A Django REST API for managing product inventory with comprehensive error handling and standardized response formats.

Live Demo: [https://simpleproduct-production.up.railway.app](https://simpleproduct-production.up.railway.app)
GitHub Repository: [https://github.com/MIYUPPIE/simple_product](https://github.com/MIYUPPIE/simple_product)

## Features

- RESTful API endpoints for product management
- UUID-based product identification
- Standardized API response format
- Rate limiting (100 requests/minute per anonymous user)
- CORS support
- Comprehensive error handling
- CI/CD pipeline with GitHub Actions
- Gunicorn production server with worker management

## Tech Stack

- Python 3.12
- Django 5.1.7
- Django REST Framework 3.14.0
- SQLite (default database)
- Gunicorn 23.0.0
- django-cors-headers 4.3.1
- python-dotenv 1.0.1
- whitenoise 6.9.0

## Prerequisites

- Python 3.12 or higher
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

Required environment variables:
- DJANGO_SECRET_KEY: Your Django secret key
- DJANGO_DEBUG: Set to False in production


5. Run migrations:
```bash
python manage.py migrate
```

6. Start the development server:
```bash
python manage.py runserver
```

For production deployment:
```bash
gunicorn business_api.wsgi:application --workers 2
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

#### Rate Limiting
- Anonymous users: 100 requests per minute
- Rate limit headers included in responses:
```
X-RateLimit-Limit: 100
X-RateLimit-Remaining: 99
X-RateLimit-Reset: 1668144600
```

## Development

### Running Tests
```bash
python manage.py test
```

### Code Style
- Follow PEP 8 guidelines
- Include docstrings for all functions
- Write unit tests for new features
- Maintain consistent error handling
- Update documentation for API changes

## Security Features

- CORS configuration with whitelisted origins
- Rate limiting enabled
- Environment variables for sensitive data
- Debug mode disabled in production
- Security middleware enabled
- HTTPS recommended for production

## Deployment

### Railway Deployment

The application is deployed on Railway. To deploy your own instance:

1. Fork the repository from [https://github.com/MIYUPPIE/simple_product](https://github.com/MIYUPPIE/simple_product)

2. Create a Railway account at [railway.app](https://railway.app)

3. Create a new project in Railway and connect your GitHub repository

4. Add the following environment variables in Railway:
   - `DJANGO_SECRET_KEY`
   - `DJANGO_DEBUG=False`
   - `DJANGO_ALLOWED_HOSTS=.up.railway.app`
   - `CORS_ALLOWED_ORIGINS`
   - `PORT=8000`

5. Add the following build command in Railway:
```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
```

6. Set the start command:
```bash
gunicorn business_api.wsgi:application --workers 2
```

7. Railway will automatically deploy your application and provide a URL

### Local Deployment

The application is configured for deployment with:
- Gunicorn as the WSGI server
- Whitenoise for static files
- Environment-based configuration
- Worker process management

### Production Configuration

Current production deployment:
- Platform: Railway
- Domain: simpleproduct-production.up.railway.app
- HTTPS: Enabled by default
- Static files: Served via Whitenoise
- Database: SQLite (consider upgrading to PostgreSQL for production)

## CI/CD

GitHub Actions workflow includes:
- Automated testing on Python 3.12
- Code linting and style checks
- Security vulnerability scanning
- Deployment automation (when configured)

## Project Structure

```
business-api/
├── business_api/        # Project configuration
│   ├── settings.py     # Django settings
│   ├── urls.py         # Main URL routing
│   └── wsgi.py         # WSGI configuration
├── products/           # Products app
│   ├── views.py       # API views
│   ├── models.py      # Data models
│   ├── serializers.py # DRF serializers
│   └── urls.py        # API endpoints
├── .env               # Environment variables
├── .env.example       # Environment template
├── requirements.txt   # Python dependencies
├── Procfile          # Deployment configuration
└── manage.py         # Django management
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[MIT License](LICENSE)

## Support

For support, please open an issue in the GitHub repository.
