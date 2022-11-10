
# How to Use Lib

settings.py
```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'ResourceAuth.Authentication.JWTBaseAuthentication',
    ]
}
RESOURCE_AUTH = {
    "jwk": "http://10.20.10.114/wOauth2/o/.well-known/jwks.json",
    "oAuth2TokenUrl": "http://10.20.10.114/wOauth2/o/token/",
    "clientId": "wisolMain",
    "clientSecret": "wisolMain"
}
```

urls append
```python

urlpatterns = [
    path('admin/', admin.site.urls),
    path("r/", include("ResourceAuth.urls"))
]
```

token Post example
```
curl --location --request POST 'http://localhost:8001/r/token/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'code=T2oXbJXllWIqYVeBfX10LIyNKbHnLZ' \
--data-urlencode 'scope=openid' \
--data-urlencode 'redirect_uri=http://localhost:8001/redirect' \
--data-urlencode 'state=5365eb78-50a1-41d9-87a8-fb1072da6674'
```

token POST Verified
```
curl --location --request POST 'http://localhost:8001/r/Verified/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'token=eyJ0eXAiOiAiSldU...'
```

