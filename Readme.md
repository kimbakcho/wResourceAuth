
# How to Use Lib

## install
```
pip install git+https://github.com/kimbakcho/wResourceAuth.git 
//upgrade
pip install --upgrade git+https://github.com/kimbakcho/wResourceAuth.git

필수 설치 lib 
corsheaders
pip install django-cors-headers
```
---
### resource 서버
```python
INSTALLED_APPS = [
    ...,
    "corsheaders",
    'ResourceAuth'
]
#corsheaders 설정
CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    ...
]

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'ResourceAuth.Authentication.JWTBaseAuthentication',
    ]
}

RESOURCE_AUTH = {
    "jwk": "http://10.20.10.114/wOauth2/o/.well-known/jwks.json"
}
```
---
### 로그인 서버
settings.py
```python

INSTALLED_APPS = [
    ...,
    "corsheaders",
    'ResourceAuth'
]
#corsheaders 설정
CORS_ALLOW_ALL_ORIGINS = True

MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware',
    ...
]

RESOURCE_AUTH = {
    "jwk": "http://10.20.10.114/wOauth2/o/.well-known/jwks.json",
    "oAuth2TokenUrl": "http://10.20.10.114/wOauth2/o/token/",
    'oAuth2RevokeUrl': "http://10.20.10.114/wOauth2/o/revoke_token/",
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
curl --location --request POST 'http://localhost:8001/r/verified/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'token=eyJ0eXAiOiAiSldU...'
```

revokeToken POST
```
curl --location --request POST 'http://localhost:9000/r/revoke/' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--header 'Cookie: csrftoken=PhCtl3HKHLPdFlg46hYyH6LA6oc8ByEv' \
--data-urlencode 'token=zlgaQynEFqKJKtnTT9....'
```

