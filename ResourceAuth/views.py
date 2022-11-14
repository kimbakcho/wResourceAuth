import requests
from django.http import HttpRequest
import jwt
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from jwt import PyJWKClient
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from .settings import api_settings
from rest_framework.views import APIView

@method_decorator(csrf_exempt, name='dispatch')
class TestView(APIView):
    def post(self,request: Request):
        response = Response({"test": "test"})
        print(response.headers)
        return response
@method_decorator(csrf_exempt, name='dispatch')
class TokenView(APIView):
    def post(self, request: Request):
        if request.data['grant_type'] == 'authorization_code':
            res = requests.post(api_settings.oAuth2TokenUrl, {
                "grant_type": request.data['grant_type'],
                "client_id": api_settings.clientId,
                "client_secret": api_settings.clientSecret,
                "redirect_uri": request.data['redirect_uri'],
                "scope": request.data['scope'],
                "state": request.data['state'],
                "code": request.data['code']
            }, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            })
            response = Response(res.json())

            return response
        elif request.data['grant_type'] == 'refresh_token':
            res = requests.post(api_settings.oAuth2TokenUrl, {
                "grant_type": request.data['grant_type'],
                "client_id": api_settings.clientId,
                "client_secret": api_settings.clientSecret,
                "scope": "openid",
                "refresh_token": request.data['refresh_token'],
            }, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            })
            return Response(res.json())
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
@method_decorator(csrf_exempt, name='dispatch')
class VerifiedView(APIView):
    jwks_client = PyJWKClient(api_settings.jwk)

    def post(self, request: Request):
        signing_key = self.jwks_client.get_signing_key_from_jwt(request.data['token'])
        data = jwt.decode(request.data['token'],
                          signing_key.key,
                          verify=True,
                          algorithms=["RS256"],
                          options={"verify_exp": True, "verify_aud": False})
        return Response(data)
@method_decorator(csrf_exempt, name='dispatch')
class RevokeTokenView(APIView):
    def post(self, request: Request):
        res = requests.post(api_settings.oAuth2RevokeUrl, {
            "token": request.data['token'],
            "client_id": api_settings.clientId,
            "client_secret": api_settings.clientSecret,
        }, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        })
        return Response(status=status.HTTP_200_OK)
