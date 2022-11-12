

from django.contrib import admin
from django.urls import path, include

from ResourceAuth.views import TokenView, VerifiedView, RevokeTokenView

urlpatterns = [
    path('token/', TokenView.as_view()),
    path('verified/', VerifiedView.as_view()),
    path('revoke/', RevokeTokenView.as_view())
]
