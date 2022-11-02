import jwt
from jwt import PyJWKClient, jwks_client
from rest_framework.authentication import BaseAuthentication
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.utils import json

from .settings import api_settings


class UserItem(object):

    def __init__(self, data: dict) -> None:
        for name, value in data.items():
            setattr(self, name, value)


class JWTBaseAuthentication(BaseAuthentication):
    www_authenticate_realm = "api"
    jwks_client = PyJWKClient(api_settings.jwk)

    def __init__(self) -> None:
        super().__init__()

    def authenticate(self, request):
        header = self.get_header(request)
        if header is None:
            return None
        raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        data = self.get_validated_token(raw_token)
        userItem = UserItem(data)
        userItem.is_authenticated = True
        return userItem, None

    def authenticate_header(self, request):
        return '{} realm="{}"'.format(
            "Bearer",
            self.www_authenticate_realm,
        )

    def get_validated_token(self, raw_token):
        signing_key = self.jwks_client.get_signing_key_from_jwt(raw_token)
        data = jwt.decode(raw_token,
                          signing_key.key,
                          algorithms=["RS256"],
                          options={"verify_exp": True, "verify_aud": False})
        return data

    def get_header(self, request):
        """
        Extracts the header containing the JSON web token from the given
        request.
        """
        header = request.META.get("HTTP_AUTHORIZATION")

        if isinstance(header, str):
            # Work around django test client oddness
            header = header.encode(HTTP_HEADER_ENCODING)

        return header

    def get_raw_token(self, header):
        """
        Extracts an unvalidated JSON web token from the given "Authorization"
        header value.
        """
        parts = header.split()

        if len(parts) == 0:
            # Empty AUTHORIZATION header sent
            return None

        if len(parts) != 2:
            raise AuthenticationFailed(
                ("Authorization header must contain two space-delimited values"),
                code="bad_authorization_header",
            )

        return parts[1]
