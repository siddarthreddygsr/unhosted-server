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
    "order_id": "2b00fef73de84b5d9f7284dccdeafcb1",
    "total": 142.3,
    "parts": [
        "LED screen",
        "Wide-Angle Camera",
        "USB-C Port",
        "Android OS",
        "Metallic Body"
    ]
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
        "order_id": "2b00fef73de84b5d9f7284dccdeafcb1",
        "total": 142.3,
        "parts": [
            "LED screen",
            "Wide-Angle Camera",
            "USB-C Port",
            "Android OS",
            "Metallic Body"
        ]
    },
    {
        "order_id": "5060dfd254e84d0bb87676d2e3dddf23",
        "total": 162.54,
        "parts": [
            "OLED screen",
            "Ultra-Wide-Angle Camera",
            "USB-C Port",
            "Android OS",
            "Metallic Body"
        ]        
    }
]
```

## Testing

Run ` python3 test.py ` to run all the unit tests