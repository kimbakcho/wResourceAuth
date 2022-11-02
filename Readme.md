
# How to Use Lib

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'ResourceAuth.Authentication.JWTBaseAuthentication',
    ]
}
```

```python
RESOURCE_AUTH = {
    "jwk": "http://localhost:8000/o/.well-known/jwks.json"
}
```

