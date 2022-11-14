
from django.conf import settings

from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, "RESOURCE_AUTH", None)

DEFAULTS = {
    "jwk": "http://10.20.10.114/wOauth2/o/.well-known/jwks.json",
    "oAuth2TokenUrl": "http://10.20.10.114/wOauth2/o/token/",
    'oAuth2RevokeUrl': "http://10.20.10.114/wOauth2/o/revoke_token/",
    "clientId": None,
    "clientSecret": None
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)


