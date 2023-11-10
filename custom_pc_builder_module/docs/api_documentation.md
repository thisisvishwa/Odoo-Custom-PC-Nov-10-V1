# Custom PC Builder Module API Documentation

This document provides a detailed description of the API endpoints, request/response formats, and example calls for the Custom PC Builder Module.

## Base URL

All URLs referenced in the API documentation have the following base:

`https://yourdomain.com/api/v1`

## Endpoints

### 1. Component Selection

- **Endpoint**: `/components`
- **Method**: `GET`
- **Response**: A list of available components.

Example:

```python
GET /api/v1/components
```

### 2. Compatibility Checker

- **Endpoint**: `/compatibility`
- **Method**: `POST`
- **Request Body**: A list of selected components.
- **Response**: A boolean indicating whether the components are compatible.

Example:

```python
POST /api/v1/compatibility
{
    "selectedComponents": ["component1", "component2", "component3"]
}
```

### 3. Price Estimation

- **Endpoint**: `/price`
- **Method**: `POST`
- **Request Body**: A list of selected components.
- **Response**: The total price of the selected components.

Example:

```python
POST /api/v1/price
{
    "selectedComponents": ["component1", "component2", "component3"]
}
```

### 4. User Account

- **Endpoint**: `/user`
- **Method**: `GET`, `POST`, `PUT`
- **Request Body** (for `POST` and `PUT`): User account details.
- **Response**: The user account details.

Example:

```python
GET /api/v1/user
POST /api/v1/user
{
    "userAccount": {
        "username": "user1",
        "email": "user1@example.com"
    }
}
PUT /api/v1/user
{
    "userAccount": {
        "username": "user1",
        "email": "user1@example.com"
    }
}
```

### 5. Order Processing

- **Endpoint**: `/order`
- **Method**: `POST`
- **Request Body**: The order details.
- **Response**: The order confirmation.

Example:

```python
POST /api/v1/order
{
    "orderDetails": {
        "user": "user1",
        "components": ["component1", "component2", "component3"],
        "totalPrice": 1000
    }
}
```

### 6. Reviews and Ratings

- **Endpoint**: `/reviews`
- **Method**: `GET`, `POST`
- **Request Body** (for `POST`): The review details.
- **Response**: The posted review (for `POST`), a list of reviews (for `GET`).

Example:

```python
GET /api/v1/reviews
POST /api/v1/reviews
{
    "reviewDetails": {
        "user": "user1",
        "component": "component1",
        "rating": 5,
        "review": "Great component!"
    }
}
```

Please note that this is a high-level overview of the API endpoints. For detailed information about each endpoint, including possible error codes and their meanings, please refer to the specific endpoint documentation.