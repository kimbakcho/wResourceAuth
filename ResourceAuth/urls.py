from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

from ResourceAuth.views import TokenView, VerifiedView, RevokeTokenView, TestView

urlpatterns = [
    path('token/', csrf_exempt(TokenView.as_view())),
    path('verified/', csrf_exempt(VerifiedView.as_view())),
    path('revoke/', csrf_exempt(RevokeTokenView.as_view())),
    path('test/', csrf_exempt(TestView.as_view()))
]
