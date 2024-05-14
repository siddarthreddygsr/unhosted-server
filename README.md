# Mobile Builder System

This is a simple Mobile Builder System implemented as an HTTP server in Python. The system allows clients to place orders for products based on selected components.

## Installation
 
### Requirements: Python3.11

` python3 app.py `

There are 2 enpoints: 
1. /orders - POST - used to order with a specific configuration
2. /get_orders - GET - get a list of all the orders

### Request:
```
POST /orders HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "components": ["A", "D", "F", "I", "K"]
}

```
### Response:
```
{
    "order_id": "27a7c447a2f44699bf07fb0073d701f1",
    "total": 150.0,
    "parts": ["LED screen", "Touchpad", "Keyboard", "Battery", "Charger"]
}
```
### Request:
```
POST /orders HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "components": ["A", "B", "F", "I", "K"]
}

```
### Response:
```
{
    "error": "Invalid choice of parts"
}
```
### Request:
```
POST /test HTTP/1.1
Host: localhost:8000
Content-Type: application/json

{
    "components": ["A", "B", "F", "I", "K"]
}

```
### Response:
```
{
    "error": "Invalid endpoint"
}
```
### Request:
```
GET /get_orders HTTP/1.1
Host: localhost:8000
```
### Response:
```
[
    {
        "order_id": "27a7c447a2f44699bf07fb0073d701f1",
        "total": 150.0,
        "parts": ["LED screen", "Touchpad", "Keyboard", "Battery", "Charger"]
    },
    {
        "order_id": "8bbfce3f16a1493bb740d0b4b4217d53",
        "total": 180.0,
        "parts": ["OLED screen", "Trackpad", "Mouse", "Adapter", "Cable"]
    }
]
```

## Testing

Run ` python3 test.py ` to run all the unit tests