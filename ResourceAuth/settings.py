
from django.conf import settings

from rest_framework.settings import APISettings

USER_SETTINGS = getattr(settings, "RESOURCE_AUTH", None)

DEFAULTS = {
    "jwk": "http://localhost:8000/o/.well-known/jwks.json"
}

api_settings = APISettings(USER_SETTINGS, DEFAULTS)

