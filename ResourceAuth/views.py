from urllib.request import Request

import requests
from django.http import HttpResponse, JsonResponse
import jwt
from django.views import View

from jwt import PyJWKClient
from .settings import api_settings

class TestView(View):
    def post(self,request: Request):
        return JsonResponse({"test": "test"})

class TokenView(View):
    def post(self, request: Request):
        if request.POST['grant_type'] == 'authorization_code':
            res = requests.post(api_settings.oAuth2TokenUrl, {
                "grant_type": request.POST['grant_type'],
                "client_id": api_settings.clientId,
                "client_secret": api_settings.clientSecret,
                "redirect_uri": request.POST['redirect_uri'],
                "scope": request.POST['scope'],
                "state": request.POST['state'],
                "code": request.POST['code']
            }, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            })

            return JsonResponse(res.json())
        elif request.POST['grant_type'] == 'refresh_token':
            res = requests.post(api_settings.oAuth2TokenUrl, {
                "grant_type": request.POST['grant_type'],
                "client_id": api_settings.clientId,
                "client_secret": api_settings.clientSecret,
                "scope": "openid",
                "refresh_token": request.POST['refresh_token'],
            }, headers={
                "Content-Type": "application/x-www-form-urlencoded"
            })
            return JsonResponse(res.json())
        else:
            return HttpResponse(status=400)

class VerifiedView(View):
    jwks_client = PyJWKClient(api_settings.jwk)

    def post(self, request: Request):
        signing_key = self.jwks_client.get_signing_key_from_jwt(request.POST['token'])
        data = jwt.decode(request.POST['token'],
                          signing_key.key,
                          verify=True,
                          algorithms=["RS256"],
                          options={"verify_exp": True, "verify_aud": False})
        return JsonResponse(data)

class RevokeTokenView(View):
    def post(self, request: Request):
        res = requests.post(api_settings.oAuth2RevokeUrl, {
            "token": request.POST['token'],
            "client_id": api_settings.clientId,
            "client_secret": api_settings.clientSecret,
        }, headers={
            "Content-Type": "application/x-www-form-urlencoded"
        })
        return HttpResponse(status=200)
