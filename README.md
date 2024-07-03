# E-commerce Microservices

## Setup

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install dependencies:
    ```
    pip install -r requirements.txt
    ```
4. Run migrations:
    ```
    python manage.py migrate
    ```
5. Create a superuser:
    ```
    python manage.py createsuperuser
    ```
6. Run the server:
    ```
    python manage.py runserver
    ```

## Docker

1. Build Docker images for each service.
2. Deploy using Kubernetes or Docker Compose.

## API Endpoints

- `POST /api/auth/register/` - Register a new user.
- `GET /api/products/` - List all products.
- `POST /api/orders/` - Create a new order.

## Testing

To run the tests, use the following command:

```bash
python manage.py test
